[Home](../README.md) · [Getting Started](getting-started.md) · [Tracks Prep](tracks-prep.md)

# Demo Song (No Licensed Audio Required)

Goal: Generate tiny test assets to validate routing (Ext. Out 13–18, IEMs/Ultranet) without real stems.

Folder scaffold
- Create `LiveTracks/Songs/DemoSong/Stems/`.

Option A — Super quick (pad only)
- Generate a 20 s pad on `17_TracksC.wav`:
  - `ffmpeg -y -f lavfi -i "sine=frequency=440:sample_rate=48000:duration=20" -ac 1 -ar 48000 -c:a pcm_s24le LiveTracks/Songs/DemoSong/Stems/17_TracksC.wav`
- In Ableton, add 2‑bar count‑in via `13_Click.wav` later, or use your DAW’s metronome while testing faders.

Option B — Add a 2‑bar count‑in click (120 BPM)
1) Generate an 20 ms click sample at 2 kHz:
   - `ffmpeg -y -f lavfi -t 0.02 -i "sine=frequency=2000:sample_rate=48000" -ac 1 tick.wav`
2) Build `13_Click.wav` with 8 ticks (bars 1–2 at 120 BPM):
   - `ffmpeg -y -i tick.wav -i tick.wav -i tick.wav -i tick.wav -i tick.wav -i tick.wav -i tick.wav -i tick.wav -filter_complex "[0:a]adelay=0|0[a0];[1:a]adelay=500|500[a1];[2:a]adelay=1000|1000[a2];[3:a]adelay=1500|1500[a3];[4:a]adelay=2000|2000[a4];[5:a]adelay=2500|2500[a5];[6:a]adelay=3000|3000[a6];[7:a]adelay=3500|3500[a7];[a0][a1][a2][a3][a4][a5][a6][a7]amix=inputs=8:normalize=0,alimiter=limit=-1.0dB" -ar 48000 -c:a pcm_s24le LiveTracks/Songs/DemoSong/Stems/13_Click.wav`
3) (Optional) Create a simple cue with macOS TTS:
   - `mkdir -p LiveTracks/Songs/DemoSong && printf "voice: Samantha\nevents:\n  - at: '0:00.0'\n    text: 'One two three four'\n" > LiveTracks/Songs/DemoSong/cues.yml`
   - `python3 tools/build_cues.py --songs LiveTracks/Songs`

Result
- You now have `13_Click.wav`, `14_Cues.wav` (optional), and `17_TracksC.wav` to import as a Scene in Ableton to verify routing to XR18 ch 13–18 and IEM/Ultranet behavior.

Cleanup
- Remove `tick.wav` if desired.

Next steps
- Build real stems via `tools/build_stems.py` or DAW export. See: `docs/tracks-prep.md`.
