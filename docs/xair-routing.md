[Home](../README.md) · [Architecture](architecture.md) · [X Air Routing](xair-routing.md) · [Ultranet](ultranet-routing.md) · [Tracks Prep](tracks-prep.md) · [Operation](operation.md) · [Troubleshooting](troubleshooting.md)

# X Air Routing (XR18)

Recommended channel map
- 1 Kick, 2 Snare, 3 Tom, 4 OH L, 5 OH R
- 6 Bass DI, 7 Guitar
- 8 Lead Vox, 9 BGV 1, 10 BGV 2
- 11 Talkback (IEM only), 12 Keys (optional)
- 13 Click (USB 13, Main LR OFF)
- 14 Cues (USB 14, Main LR OFF)
- 15 Tracks 1 (Perc/Loops)
- 16 Tracks 2 (Synth/Bass)
- 17 Tracks 3 (Keys/Pads)
- 18 Tracks 4 (BGV/FX)

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
- No live drummer: set ch 1–5 Source = USB (Card 1–5). For stereo drums only, use Card 4/5.

3) IEM sends
- Buses 1–5: set Send Tap = Pre‑EQ (so FOH tweaks don’t change IEMs).
- Build each performer’s mix by raising sends from the needed channels.
- Talkback mic (e.g., ch 11): Main LR OFF; send to IEM buses only.

4) Outputs
- Aux Out 1–5 → Bus 1–5 (default). Connect to IEM transmitters/amps at line level.
- Save a base Scene, e.g., XR18_LiveTracks_Base.scn.

Helpful screenshots
- Channel view: Source selector (USB vs Analog).
- Sends view: Main LR OFF on ch 13–14; bus tap set to Pre‑EQ.

[Home](../README.md) · [Architecture](architecture.md) · [X Air Routing](xair-routing.md) · [Ultranet](ultranet-routing.md) · [Tracks Prep](tracks-prep.md) · [Operation](operation.md) · [Troubleshooting](troubleshooting.md)

