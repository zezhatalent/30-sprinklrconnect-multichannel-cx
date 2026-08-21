import json
import os

import requests
from dotenv import load_dotenv

load_dotenv()

with open("channel_map.json", encoding="utf-8") as f:
    MAP = json.load(f)

SAMPLE_CASES = [
    {"channel": "twitter", "text": "worst service ever, this is unacceptable @brand"},
    {"channel": "whatsapp", "text": "hi, my refund is pending from 10 days"},
    {"channel": "email", "text": "kindly share GST invoice for August order"},
    {"channel": "facebook", "text": "do you deliver to Nagpur?"},
]


def route(case: dict) -> dict:
    channel = case.get("channel", "email").lower()
    q = MAP["queues"].get(channel, {"queue": MAP["default_queue"], "sla_hours": 24})
    text = case.get("text", "").lower()
    urgent = any(k in text for k in MAP["urgency_keywords"])
    return {
        "queue": q["queue"] if not urgent else "priority_escalation",
        "sla_hours": q["sla_hours"] if not urgent else 1,
        "urgent": urgent,
    }


def push_to_sprinklr(case: dict, decision: dict):
    token = os.environ.get("SPRINKLR_TOKEN")
    if not token:
        return None
    base = os.environ.get("SPRINKLR_BASE_URL", "https://api2.sprinklr.com")
    resp = requests.post(
        f"{base}/api/v2/case",
        headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"},
        json={"case": case, "routing": decision},
        timeout=30,
    )
    return resp.json()


if __name__ == "__main__":
    print("SprinklrConnect Router — routing decisions (offline demo):\n")
    for case in SAMPLE_CASES:
        d = route(case)
        print(f"[{case['channel']:8}] urgent={d['urgent']} -> {d['queue']} (SLA {d['sla_hours']}h)")
        print(f"           \"{case['text'][:60]}\"\n")
