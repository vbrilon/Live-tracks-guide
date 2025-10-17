# Live Backing Tracks with XR18 + Ableton (Mac)

This is the master doc. Use the links below to jump into focused guides.

Start here
- Overview & concepts: [Architecture & Explanation](docs/architecture.md)
- X Air routing: [X Air Routing](docs/xair-routing.md)
- Ultranet routing: [Ultranet Routing](docs/ultranet-routing.md)
- Preparing tracks (Logic, Ableton, Ableset): [Tracks Prep](docs/tracks-prep.md)
- Running the show: [Operation](docs/operation.md)
- Troubleshooting: [Troubleshooting](docs/troubleshooting.md)

Hardware & software checklist
- Mac laptop with Ableton Live and Ableset
- Logic Pro (for tempo map, click, cues)
- XR18 on latest firmware; X Air Edit on the Mac
- USB‑B cable XR18 ⇄ Mac; TRS to your IEM transmitters/amps
- Optional: P16‑M personal mixers + P16‑D; MIDI foot controller

Quick reference
- Sample rate 48 kHz; Buffer 128–256
- Ableton outputs: Click 13, Cues 14, Stems 15–18 → XR18 ch 13–18 (USB)
- Instrument‑swappable (any instrument): keep the same channel number (e.g., Bass → 6, Guitar → 7, Keys → 12; Drums → 1–5 if tracked) and flip XR18 Source (Analog ↔ USB). Remove that instrument from stems to avoid doubles.
- Safety: “Main LR” OFF on Click/Cues

TODO
- Add analog IEM bus variant diagram and routing steps
- Add screenshots (X Air Edit, Ultranet, Ableton, Ableset, Logic exports)
  - Temporary vendor image used for Ableset setlist preview; replace with your own captures
  - Capture and place screenshots into `Assets/img/screenshots/` with these filenames:
    - `xair-setup-audio-48k.png`, `xair-channel-13-mainlr-off.png`, `xair-channel-15-usb.png`, `xair-buses-pre-eq-tap.png`, `xair-routing-ultranet-grid.png`
    - `ableton-prefs-output-config.png`, `ableton-track-io-ext-out-13-18.png`, `ableton-clip-warp-off.png`
    - `ableset-setlist.png`, `ableset-midi-mapping.png`
    - `logic-smart-tempo.png`, `logic-export-all-tracks.png`
- Add templates: Logic prep template and Ableton .als pre‑routed (06/07/13–18)
