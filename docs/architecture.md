[Home](../README.md) · [Architecture](architecture.md) · [X Air Routing](xair-routing.md) · [Ultranet](ultranet-routing.md) · [Tracks Prep](tracks-prep.md) · [Operation](operation.md) · [Troubleshooting](troubleshooting.md)

# Architecture & Explanation

![System Diagram — Mac ↔ XR18 USB, Ultranet P16‑M](../Assets/img/system-diagram.svg)

Plain‑language concepts
- XR18 = mixer + USB audio interface. It receives up to 18 channels from the Mac and can send 18 channels back to the Mac.
- Ableton plays stems (separate audio files per part) plus Click and Cues.
- Each stem goes to an Ableton output number (e.g., Ext. Out 15) that lands on the identically numbered XR18 channel (ch 15).
- FOH mixes stems (15–18) to the mains. Click and Cues (13–14) are for IEMs only and must never hit Main LR.
- IEM options:
  - Ultranet: P16‑M personal mixers get up to 16 channels from the XR18’s Ultranet port.
  - Analog IEM buses: XR18 Buses 1–5 feed Aux Outs 1–5 to your transmitters/amps.

Why 48 kHz and a 128–256 buffer?
- XR18 defaults to 48 kHz. Keep everything at 48 kHz to avoid resampling and clock issues.
- 128–256 buffer is a good live balance: low latency but stable. If you hear pops/clicks, try 256.

Terminology (assume no prior knowledge)
- Card/USB: audio coming from the computer into the XR18.
- Tap point: where a send takes signal from a channel. Pre‑EQ means FOH EQ/fader won’t change the IEM feed.
- DirOut Ch X: direct output of channel X (not a bus or the mains).

Helpful screenshots to capture
- X Air Edit → Setup → Audio/MIDI with 48 kHz selected.
- macOS Audio MIDI Setup showing the XR18 device present.

[Home](../README.md) · [Architecture](architecture.md) · [X Air Routing](xair-routing.md) · [Ultranet](ultranet-routing.md) · [Tracks Prep](tracks-prep.md) · [Operation](operation.md) · [Troubleshooting](troubleshooting.md)

