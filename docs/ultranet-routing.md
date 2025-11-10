[Home](../README.md) · [Getting Started](getting-started.md) · [Architecture](architecture.md) · [X Air Routing](xair-routing.md) · [Ultranet](ultranet-routing.md) · [Tracks Prep](tracks-prep.md) · [Reaper Batch Prep](reaper-batch-prep.md) · [Operation](operation.md) · [Troubleshooting](troubleshooting.md)

# Ultranet Routing (XR18 → P16‑M)

Summary: Map XR18 sources to Ultranet slots for P16‑M mixers, with options to save slots via bus submixes and preserve channel consistency.

Ultranet carries 16 mono channels to personal mixers. Assign XR18 sources to Ultranet slots so each musician builds their own IEM mix without FOH changes affecting them.

Important: P16‑M replaces XR18 IEM Buses for those users
- When a musician uses a P16‑M, you don’t need to create a separate IEM Bus for them on the XR18. Their IEMs can plug directly into the P16‑M headphone output, or the P16‑M line out can feed a wireless transmitter.
- Keep using XR18 IEM Buses for any players NOT on P16s (e.g., analog IEMs or wedges). Mixed setups (some P16, some Bus) work fine.

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
 - Drum tracks: if you use mono drums, deliver them on slot 4 (matching ch 4). For stereo drums, use slots 4/5. For multi‑stem drums, keep 1–5 as listed.

Using a Bus to feed P16 (Drums Submix)
- Why: Save Ultranet slots and give musicians a single “Drums” knob on the P16 instead of multiple drum channels.
- Pick a free bus (e.g., Bus 6 if Buses 1–5 are used for analog IEMs).
- On Kick/Snare/Tom/OH channels, raise the send to that bus to create your preferred drum balance.
- Set the bus Send Tap to Pre‑EQ if you don’t want FOH EQ/faders to affect the P16 submix, or Post‑EQ if you do.
- Routing → Ultranet: assign an Ultranet slot (e.g., 4) to Source = Bus 6, Tap = Pre‑EQ. Label it “Drums”.
- Result: P16 shows one channel for the entire drum kit; FOH still gets individual drum channels for mixing.

New to Buses? See “Buses 101” in [X Air Routing](xair-routing.md) for concepts, tap choices, and “Sends on Faders” mixing.

P16 / IEM enhancements
- Presets per player: save each musician’s P16 mix as a preset so their balances survive power cycles. Label presets on tape for fast recall.
- Additional bus submix patterns:
  - BGV blend bus → one P16 slot (save slots for other needs)
  - Keys + Pads blend bus → one P16 slot (FOH still receives individual channels if routed that way)
- Tap trade‑offs: Pre‑EQ taps keep IEMs stable regardless of FOH moves; Post‑EQ taps let FOH tonal changes flow to IEMs—choose per performer preference.

Helpful screenshots
- Routing → Ultranet grid showing slot sources and Pre‑EQ taps.

  ![X Air Edit — Ultranet slot routing](../Assets/img/screenshots/xair-routing-ultranet-grid.png)

  Note: TODO — replace with your own screenshot (Routing → Ultranet).
  Reference manual (PDF): https://usermanual.wiki/Document/XAIREditOperationManual.790879087.pdf

Next step: [Tracks Prep](tracks-prep.md)

[Home](../README.md) · [Getting Started](getting-started.md) · [Architecture](architecture.md) · [X Air Routing](xair-routing.md) · [Ultranet](ultranet-routing.md) · [Tracks Prep](tracks-prep.md) · [Reaper Batch Prep](reaper-batch-prep.md) · [Operation](operation.md) · [Troubleshooting](troubleshooting.md)
