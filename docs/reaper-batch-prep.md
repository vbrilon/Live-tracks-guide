[Home](../README.md) · [Getting Started](getting-started.md) · [Architecture](architecture.md) · [X Air Routing](xair-routing.md) · [Ultranet](ultranet-routing.md) · [Tracks Prep](tracks-prep.md) · [Reaper Batch Prep](reaper-batch-prep.md) · [Operation](operation.md) · [Troubleshooting](troubleshooting.md)

# Reaper Batch Prep (Optional, For Large Catalogs)

Reaper excels when you need to prepare many songs quickly and consistently. With SWS Extensions, you can tempo‑map, place markers/regions, and batch‑render click, cues, and stems for dozens of songs in one pass with standardized filenames.

## Why choose Reaper instead of Logic
- Batch at scale: Region Render Matrix exports many songs × many tracks in one click; Logic can’t batch across projects like this.
- Tight naming control: Wildcards auto‑name by song/region and track (e.g., `13_Click`, `14_Cues`, `15_TracksA`).
- Tempo‑aware click printing: Insert a “Click source” that follows your tempo map—no metronome printing hassles.
- Scriptable workflow: SWS actions streamline repetitive mapping/marking steps.

Use Reaper when
- You’re onboarding tens/hundreds of songs from MP3s or live recordings.
- You want a reproducible pipeline that outputs correctly named 48 kHz / 24‑bit WAVs every time.

Consider Logic or Ableton‑only when
- Logic: best for a handful of variable‑tempo songs leveraging Smart Tempo.
- Ableton‑only: fastest for steady‑tempo material already on‑grid at 48 kHz.

## Core concepts you’ll use
- Regions: one region per song (start/end). Keep many songs in one Reaper project.
- Region Render Matrix: choose which tracks to render for which regions.
- Wildcards: auto‑name files by region and track (e.g., `$region_$track.wav`).
- SWS Extensions: adds actions to speed tempo mapping and region management.

## Minimal Reaper recipe (many songs in one project)
1) Setup
- Install Reaper + SWS. Set project sample rate to 48 kHz.
- Create a template with tracks named to match the channel plan:
  - `13_Click`, `14_Cues`, `15_TracksA`, `16_TracksB`, `17_TracksC`, `18_TracksD`
  - Optional dedicates: `06_Bass`, `07_Guitar`, `12_Keys`
  - Optional `Master_Reference` (stereo MP3 or guide mix)

2) Tempo map each song
- Import the reference (MP3 or stereo stem) to `Master_Reference`.
- Place downbeat markers and adjust the tempo map, or use SWS/BR actions to warp grid to item transients.
- Create a Region covering the song (Region/Marker Manager). Name it exactly as the song (e.g., `01 Run Away`).

3) Build click and cues
- Click: Insert → Click source on `13_Click` (follows the tempo map; set accent on bar 1).
- Cues: Place/record spoken cue items on `14_Cues` aligned to bar markers.
- Stems: Place printed stems on `15–18` (and `06/07/12` if promoting instruments). Keep peaks around −6 dBFS.

4) Repeat for all songs
- Put each song back‑to‑back on the timeline with its own Region.
- Reuse the same tracks for every song.

5) Batch render with Region Render Matrix
- Render dialog:
  - Source: Region render matrix
  - Bounds: All project regions
  - Sample rate / Bit depth: 48 kHz / 24‑bit; Dither Off; Normalize Off
  - Channels: Mono for mono tracks; Stereo where needed
  - Wildcards: `$region_$track.wav`
- Region Render Matrix: tick each Region × Track you wish to render.
- Render to `LiveTracks/Songs/<SongName>/Stems/` (you can set per‑region output directories).

6) Assemble in Ableton + Ableset
- In Ableton, disable Auto‑Warp. Create standard tracks and route to `Ext. Out 13–18` (and 06/07/12 if used).
- Drag each song’s files into one Scene; name Scenes `01 <SongName>`, `02 <SongName>`, etc. Ableset reads Scenes as songs automatically.

## Pros and cons
- Pros: Massive speed‑up for batches; one pass renders everything; predictable names; click source synced to tempo map.
- Cons: Learning curve; tempo mapping is less “automatic” than Logic Smart Tempo; more initial template work.

## Implementation support (what we can add next)
- Provide a Reaper template project (`.RPP`) with tracks pre‑named (`13_Click`, `14_Cues`, `15_TracksA`, etc.), a basic click source, and Region Render Matrix presets.
- Include a wildcard/naming cheatsheet and suggested Render settings.
- Short SWS action list to accelerate common steps (e.g., create regions from markers, warp grid to item, batch marker utilities).
- A 10‑minute starter walkthrough: from importing an MP3 to batch rendering click/cues/stems for 3 songs.

[Home](../README.md) · [Getting Started](getting-started.md) · [Architecture](architecture.md) · [X Air Routing](xair-routing.md) · [Ultranet](ultranet-routing.md) · [Tracks Prep](tracks-prep.md) · [Reaper Batch Prep](reaper-batch-prep.md) · [Operation](operation.md) · [Troubleshooting](troubleshooting.md)

