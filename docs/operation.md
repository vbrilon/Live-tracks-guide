[Home](../README.md) · [Getting Started](getting-started.md) · [Architecture](architecture.md) · [X Air Routing](xair-routing.md) · [Ultranet](ultranet-routing.md) · [Tracks Prep](tracks-prep.md) · [Reaper Batch Prep](reaper-batch-prep.md) · [Operation](operation.md) · [Troubleshooting](troubleshooting.md)

# Operation (Bringing It All Together)

Summary: Soundcheck and show‑time steps, safe break‑music Scenes, quick reference, and gain/IEM safety notes.

Power‑up and line check
- Power order: XR18 → connect USB → launch Ableton/Ableset → load set.
- Verify live mics/instruments (1–12).

Tracks check
- Play a song; confirm:
  - Click (ch 13) only in IEMs (Main LR OFF)
  - Cues (ch 14) only in IEMs (Main LR OFF)
  - Stems (15–18) audible in FOH and IEMs
- Gain stage around 0 dB on meters; avoid red.

Virtual soundcheck
- With the band muted, play stems to set FOH and IEM balances safely.
- For IEMs, use Sends‑on‑Faders on each Bus to mix the performer’s balance; keep Bus taps Pre‑EQ so FOH tweaks don’t shift their monitors.

Show operation
- Use Ableset or your footswitch to start/stop/advance scenes.
- If Ableset fails, trigger Scenes directly in Ableton as a fallback.

Between‑set music (Mac via USB)
- Set Mac system output device to XR18 (macOS Sound settings).
- On XR18, load your Break Music Scene (maps USB 1/2 → ch 17/18).
- Play Spotify/Apple Music/etc.; adjust level on ch 17/18 faders.
- Before resuming the show, load your Performance Scene (maps USB 17/18 → ch 17/18 for stems).
- Tip: In the Break Music Scene, set ch 1/2 Source = Analog (or mute ch 1/2) so USB 1/2 only feeds ch 17/18 and doesn’t also show up on ch 1/2.

Practical safety tips
- Tape labels for 13–18 on the XR18; mark Click/Cues “IEM only”.
- Keep Wi‑Fi off unless needed; prefer wired network for OSC.
- Bring a backup USB cable and a small power conditioner for the Mac.

Quick reference
- Sample rate 48 kHz; Buffer 128–256
- Ableton outputs: Click 13, Cues 14, Stems 15–18 → XR18 ch 13–18 (USB)
- Ultranet P16: 1–10 live channels; 11 Click; 12 Cues; 13–16 stems
- Instrument‑swappable (any instrument): keep the same channel number (e.g., Bass → 6, Guitar → 7, Keys → 12) and flip XR18 Source (Analog ↔ USB). Remove that instrument from stems to avoid doubles.
- Drums preferred map: Kick 1, Snare 2, Tom 3, OH L 4, OH R 5; stereo fallback 4/5
- Drum tracks (no live drummer): mono fallback 4; stereo fallback 4/5
- IEMs: Either XR18 Buses (1–5, mono, Pre‑EQ; Aux Out 1–5 → IEM chain) or P16‑M over Ultranet (no Bus required for those players)
- Safety: “Main LR” OFF on Click/Cues

Gain staging & calibration (recommended)
- Before soundcheck, set Ableton clip Gains so XR18 channel meters read near 0 dB with faders near unity.
- Optional pink‑noise sanity check: add a −18 dBFS pink noise clip to Ableton, route it to a stem channel (e.g., ch 15), and bring Main LR to a comfortable reference level in the room. Mark the mains position for repeatability.
- TODO: add `Assets/audio/pink-noise-18dBFS.wav` to the repo for quick use.

IEM safety
- Keep bus taps Pre‑EQ for IEMs so FOH tweaks don’t surprise players.
- Consider a gentle bus compressor/limiter on each IEM bus (or insert a limiter FX) to catch unexpected peaks. Set conservatively to avoid pumping.
- Verify Click level is comfortable; label Click/Cues clearly and keep them out of mains.

Next step: [Troubleshooting](troubleshooting.md)

[Home](../README.md) · [Getting Started](getting-started.md) · [Architecture](architecture.md) · [X Air Routing](xair-routing.md) · [Ultranet](ultranet-routing.md) · [Tracks Prep](tracks-prep.md) · [Reaper Batch Prep](reaper-batch-prep.md) · [Operation](operation.md) · [Troubleshooting](troubleshooting.md)
