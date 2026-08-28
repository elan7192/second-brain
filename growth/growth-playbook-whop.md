---
type: growth
tags:
  - growth
created: 2026-08-25
updated: 2026-08-25
growth_layer: playbooks
---

# Playbook: Whop CLI

Command shapes from [[src-deronin-growthos-vault]]. Hub: [[growth-playbooks]]. **Do not run against a live account from this vault.**

## Setup prompt (human pastes)

Install the Whop CLI, sign in, and run `whop skills add`
- then run `whop --llms` and say in your own words what you can and cannot do with this login
- list what is already on this account. If you find products the human did not create, leave them alone and report them
- report anything Whop turns on by default that was not asked for

## Offer prompt (AI UGC example)

```yaml
Set up the offer on Whop for this creator:
- AI UGC Community, $49/mo, subscription
- Starter Pack (templates + presets), $149, one time
- 1:1 Audit, $299, one time
- create a checkout link for each one and give me the three URLs
- don't touch anything belonging to another business on this account
```

## Commands cited

```bash
whop products list
whop plans create --help
whop checkout-configurations create --plan_id plan_xxx
whop stats time_series
```

Every command takes `--format json`. See [[growth-ruling-no-money]].
