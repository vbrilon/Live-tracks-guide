[Home](../README.md) · [Architecture](architecture.md) · [X Air Routing](xair-routing.md) · [Ultranet](ultranet-routing.md) · [Tracks Prep](tracks-prep.md) · [Operation](operation.md) · [Troubleshooting](troubleshooting.md)

# Ultranet Routing (XR18 → P16‑M)

Ultranet carries 16 mono channels to personal mixers. Assign XR18 sources to Ultranet slots so each musician builds their own IEM mix without FOH changes affecting them.

How to assign
- In X Air Edit: Routing → Ultranet.
- For each slot 1–16: Source = DirOut Ch X (or Card/Bus as needed); Tap = Pre‑EQ.
- Store as a Scene once verified.

Recommended Ultranet map (4 stems)
- 1 Kick, 2 Snare, 3 Tom, 4 OH L, 5 OH R
- 6 Bass (live or backing), 7 Guitar
- 8 Lead Vox, 9 BGV 1, 10 BGV 2
- 11 Click (from ch 13 USB), 12 Cues (from ch 14 USB)
- 13 Tracks A (Perc/Loops, ch 15 USB)
- 14 Tracks B (Synth/Bass, ch 16 USB)
- 15 Tracks C (Pads/FX, ch 17 USB)
- 16 Tracks D (BGV/FX, ch 18 USB)

Notes and variants
- Keep Click/Cues out of Main LR; Ultranet is independent of mains.
- Talkback is not mapped above. If needed on P16, repurpose a slot (e.g., collapse OH to mono) or feed talkback via a shared bus.
- Channel consistency (must do): For any instrument you swap (Bass 6, Guitar 7, Keys 12, Drums 1–5), keep the same XR18 channel number and the same Ultranet slot. Only flip the channel Source (Analog ↔ USB) and route Ableton to that channel’s number.
- Avoid duplication: when promoting any instrument to a dedicated channel, remove it from the stems feeding 15–18 so P16 users don’t hear doubles.

Helpful screenshots
- Routing → Ultranet grid showing slot sources and Pre‑EQ taps.

  ![X Air Edit — Ultranet slot routing](../Assets/img/screenshots/xair-routing-ultranet-grid.png)

  Note: TODO — replace with your own screenshot (Routing → Ultranet).

[Home](../README.md) · [Architecture](architecture.md) · [X Air Routing](xair-routing.md) · [Ultranet](ultranet-routing.md) · [Tracks Prep](tracks-prep.md) · [Operation](operation.md) · [Troubleshooting](troubleshooting.md)
