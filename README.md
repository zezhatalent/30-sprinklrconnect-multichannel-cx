# SprinklrConnect Router — Multi-Channel Case Routing
### Built on the Sprinklr API (live integration + offline demo)

**Category:** Omnichannel CX Operations | **Deployment:** Sprinklr Cloud + Your Router | **Sector:** Consumer brands, BFSI, telecom with social + messaging presence

---

## Overview

SprinklrConnect routes inbound cases across **Twitter/X, Facebook, WhatsApp and
email** to the right Sprinklr queue with channel-specific SLAs — and escalates
urgency keywords ("fraud", "unacceptable", "legal notice") into a priority queue
with a 1-hour SLA.

Runs offline on sample cases today; flips to live Sprinklr case creation with one
API token.

## Key Features

- Channel-aware queue mapping with per-channel SLA hours
- Urgency keyword engine overrides routing to priority escalation
- Live push to Sprinklr Case API when token configured
- Demo runner showing decisions for 4 realistic Indian-brand cases

## Business Value

| Metric | Impact |
|--------|--------|
| Social-media risk | Angry public posts get 1-hour response SLA |
| Consistency | Every channel routed by one policy file |
| Auditability | Decisions computed from config, not memory |

## How It Works

```
Inbound Case (any channel) ──► route() ──► queue + SLA ──► Sprinklr Case API (optional live)
```

## Technical Requirements

- Sprinklr account with API access for live mode (client-provided)
- Python 3.10+

## Installation & Setup — Step by Step

```powershell
cd 30-sprinklrconnect-multichannel-cx
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt

# Offline demo:
python sprinklr_case_router.py

# Live mode:
copy .env.example .env    # add SPRINKLR_TOKEN
```

## Customization for Your Business

- Edit `channel_map.json`: add Instagram, Play Store reviews, Telegram queues
- Tune urgency keywords; add Hinglish variants ("turant", "foran")
- Add business-hours-aware SLA calculation

## What's Included

- Routing engine (`sprinklr_case_router.py`)
- Channel/SLA policy (`channel_map.json`)
- Documentation and 1 customization session

---

*One routing brain for every channel your customers complain on.*
