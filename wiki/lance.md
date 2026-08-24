---
type: concept
tags:
  - wiki
created: 2026-08-24
updated: 2026-08-24
---
# LANCE

One-shot HOSVD activation cores for last-2/4-layer on-device fine-tune and CL.

Source: [[src-arxiv-2509-21617]]. Project: [[arxiv-tierlist]].

## Kept

MCUNet CIFAR-10: up to ~250× activation memory, 3–7pt accuracy drop. Split CIFAR-100: near GPM (71.52 vs 72.48), well below CODE-CL 77.21, 2.32 MB vs 22–33 MB.

Last layers only. Not full-network training from scratch on a microcontroller.

## Related

[[arxiv-tierlist]]
