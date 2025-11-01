# Live Backing Tracks with XR18 + Ableton (Mac)

This is the master doc. Use the links below to jump into focused guides.

Start here
- First-time setup: [Getting Started](docs/getting-started.md)
- Overview & concepts: [Architecture & Explanation](docs/architecture.md)
- X Air routing: [X Air Routing](docs/xair-routing.md)
- Ultranet routing: [Ultranet Routing](docs/ultranet-routing.md)
- Preparing tracks (Logic, Ableton, Ableset): [Tracks Prep](docs/tracks-prep.md)
- Bulk import from MP3 folders: [Automation (Bulk Import)](docs/automation-bulk-import.md)
- Generate tempo maps from click: [Tempo Map From Click](docs/tempo-map-from-click.md)
- Batch prep at scale: [Reaper Batch Prep](docs/reaper-batch-prep.md)
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
- Drum tracks (no live drummer): mono fallback 4; stereo fallback 4/5
- Safety: “Main LR” OFF on Click/Cues
 - IEM safety: taps Pre‑EQ; consider a gentle compressor/limiter on IEM buses

Ultranet tip
- To save P16 slots, create a mono “Drums” submix on a free bus (e.g., Bus 6) and assign that bus to one Ultranet slot. Musicians get one drum knob while FOH retains individual drum channels.

Break music (between sets)
- macOS system audio plays on USB 1/2. Create two XR18 Scenes to flip ch 17/18 Source:
  - Performance Scene: ch 17/18 Source = USB 17/18 (stems)
  - Break Music Scene: ch 17/18 Source = USB 1/2 (Mac apps like Spotify)
- Load Break Music Scene for PA music; load Performance Scene before resuming the show.
 - In the Break Music Scene, set ch 1/2 Source = Analog (or mute ch 1/2) so USB 1/2 only feeds ch 17/18.

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
 - Image hotlinks (for reference now; replace with local later)
   - X Air Edit manual (PDF): https://usermanual.wiki/Document/XAIREditOperationManual.790879087.pdf
   - Ableton Audio Preferences: https://help.ableton.com/hc/en-us/articles/209068929-Audio-Preferences
   - Ableton Warping in Live: https://help.ableton.com/hc/en-us/articles/209773265-Warping-in-Live
   - Logic Pro Smart Tempo: https://support.apple.com/guide/logicpro/smart-tempo-overview-lgcpbbef4bfc/mac
   - Logic Pro Export Projects: https://support.apple.com/guide/logicpro/export-projects-lgcp2ea17c68/mac
   - Ableset site: https://www.ableset.app/
