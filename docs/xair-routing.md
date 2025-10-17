[Home](../README.md) · [Architecture](architecture.md) · [X Air Routing](xair-routing.md) · [Ultranet](ultranet-routing.md) · [Tracks Prep](tracks-prep.md) · [Operation](operation.md) · [Troubleshooting](troubleshooting.md)

# X Air Routing (XR18)

Recommended channel map
- 1 Kick, 2 Snare, 3 Tom, 4 OH L, 5 OH R
- 6 Bass DI, 7 Guitar
- 8 Lead Vox, 9 BGV 1, 10 BGV 2
- 11 Spare/Utility, 12 Keys (optional)
- 13 Click (USB 13, Main LR OFF)
- 14 Cues (USB 14, Main LR OFF)
- 15 Tracks 1 (Perc/Loops)
- 16 Tracks 2 (Synth/Bass)
- 17 Tracks 3 (Pads/FX)
- 18 Tracks 4 (BGV/FX)

Consistency rules (live ↔ tracks)
- For any instrument, the channel number stays the same whether it’s live or from tracks. You only flip the XR18 channel Source (Analog ↔ USB) and route Ableton to that exact channel number.
- Examples: Bass → ch 6, Guitar → ch 7, Keys → ch 12, Drums → ch 1–5 (if running drum tracks, route Kick/Snare/Tom/OH to 1–5 and remove drums from stems on 15–18).
- Avoid duplication: when you promote any instrument to its dedicated channel, remove it from the stems so it isn’t doubled (e.g., if Keys are on ch 12, do not include Keys inside the stem feeding ch 17).

Drum tracks variants (no live drummer)
- Preferred mono: route a single summed Drum track to ch 4 (USB Card 4). Park/mute ch 1, 2, 3, and 5.
- Stereo option: route `Drums L` → ch 4 and `Drums R` → ch 5. Park/mute ch 1–3.
- Multi‑stem option: if you exported Kick/Snare/Tom/OH, route them to ch 1–5 respectively (keep Keys/other stems out of 15–18 accordingly).

Step‑by‑step in X Air Edit (Mac)
1) Global
- Setup → Audio/MIDI → Sample Rate: 48 kHz.
- Confirm macOS sees the XR18 as an audio device.

2) Channel sources
- On ch 13–18, set Source = USB (Card). On ch 1–12, keep Source = Analog.
- On ch 13 (Click) and 14 (Cues): turn OFF Main LR.
- On ch 15–18 (stems): keep Main LR ON; start faders around −10 dB.
- Instrument‑swappable channels (e.g., Bass ch 6, Guitar ch 7):
  - Backing → set Source = USB (Card 6/7)
  - Live player → set Source = Analog
- No live drummer:
  - Mono summed drums → set ch 4 Source = USB (Card 4); park/mute ch 1, 2, 3, 5.
  - Stereo drums → set ch 4/5 Source = USB (Card 4/5); park/mute ch 1–3.
  - Multi‑stem drums → set ch 1–5 Source = USB (Card 1–5).

3) IEM sends
- Buses 1–5: set Send Tap = Pre‑EQ (so FOH tweaks don’t change IEMs).
- Build each performer’s mix by raising sends from the needed channels.

4) Outputs
- Aux Out 1–5 → Bus 1–5 (default). Connect to IEM transmitters/amps at line level.
- Save a base Scene, e.g., XR18_LiveTracks_Base.scn.

Helpful screenshots
- Channel view: Source selector (USB vs Analog).

  ![X Air Edit — Channel Source set to USB](../Assets/img/screenshots/xair-channel-15-usb.png)

  Note: TODO — replace with your own screenshot showing ch 15 set to USB (Card 15).
  Reference manual (PDF): https://usermanual.wiki/Document/XAIREditOperationManual.790879087.pdf

- Ch 13–14 with Main LR OFF (Click/Cues safety).

  ![X Air Edit — Ch 13 Main LR OFF](../Assets/img/screenshots/xair-channel-13-mainlr-off.png)

  Note: TODO — replace with your own screenshot for both ch 13 and 14.
  Reference manual (PDF): https://usermanual.wiki/Document/XAIREditOperationManual.790879087.pdf

- Bus sends tap set to Pre‑EQ.

  ![X Air Edit — Bus Sends Tap Pre‑EQ](../Assets/img/screenshots/xair-buses-pre-eq-tap.png)

  Note: TODO — replace with your own screenshot (Bus Sends gear → Pre‑EQ).
  Reference manual (PDF): https://usermanual.wiki/Document/XAIREditOperationManual.790879087.pdf

- Setup → Audio/MIDI at 48 kHz.

  ![X Air Edit — Setup 48 kHz](../Assets/img/screenshots/xair-setup-audio-48k.png)

  Note: TODO — replace with your own screenshot.
  Reference manual (PDF): https://usermanual.wiki/Document/XAIREditOperationManual.790879087.pdf

[Home](../README.md) · [Architecture](architecture.md) · [X Air Routing](xair-routing.md) · [Ultranet](ultranet-routing.md) · [Tracks Prep](tracks-prep.md) · [Operation](operation.md) · [Troubleshooting](troubleshooting.md)
