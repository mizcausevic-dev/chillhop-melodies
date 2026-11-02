# Chillhop Melodies

Original note-only MIDI studies of concise melodies. Eight studies, two variations of the melody. Each study is 8 bars: a short motif, a melodic answer, and space for accompaniment. Keys references and bass references are cataloged separately and are not part of the core count. They are not merged into the melody files.

This repository is the pack. The GitHub repository is https://github.com/mizcausevic-dev/chillhop-melodies and it is public. The catalog page is https://mizcausevic-dev.github.io/chillhop-melodies/ .

## What you can open

- `index.html` is the file catalog. The melody roll is drawn from the melody MIDI bytes. Keys and bass are separate toggles.
- `media.html` is the stills page. The film sits under the pictures.
- `midi/arrangement.mid` is a Format 1 preview arrangement of study 01, variation A: melody, keys reference, and bass reference.
- Individual Format 0 parts live under `midi/`.
- `midi/validation-Cursor.json` is the report from reopening those exact bytes.
- `preview/preview.mp3` is the primary music preview. It is 24.615 seconds in the encoded file. preview, not a master.
- `film/preview.mp4` and `film/preview.vtt` are the film. On-picture and caption text is `preview, not master`.
- `art/hero.jpg` is a 1280x720 illustration. `art/square.jpg` is 1080x1080. Neither is a photograph.

Use either the combined arrangement or the separate parts. Do not stack the part files on top of the combined file.

## Studies

- s01 Second Sixteenth: 78 BPM, 8 bars, D dorian, tonic reference D.
- s02 And of Two: 84 BPM, 8 bars, A natural minor, tonic reference A.
- s03 Held Answer: 72 BPM, 8 bars, F major, tonic reference F.
- s04 Fifth Then Rest: 90 BPM, 8 bars, G mixolydian, tonic reference G.
- s05 Question Rest: 76 BPM, 8 bars, C major, tonic reference C.
- s06 Step and Leap: 86 BPM, 8 bars, E natural minor, tonic reference E.
- s07 Soft Cadence: 70 BPM, 8 bars, Bb major, tonic reference Bb.
- s08 Open Space: 94 BPM, 8 bars, B natural minor, tonic reference B.

Core files: 16. Reference files: 32.

Melody is the core, monophonic, MIDI 55 to 86. Keys references use MIDI 40 to 76, at most four notes at once, and are not core. Bass references are monophonic, MIDI 28 to 52, and are not core. C4 is 60. PPQ is 960. Meter is 4/4. Offsets are 0. The pocket is the written grid. Random jitter is not groove. Tape dust is not a note. Seeds identify studies and are not random draws. Generator 1.0.0. Eight bars for every study. Sixteen bars at 70-95 BPM lasts about 40.4 seconds or longer.

## Preview path

The preview renders the canonical notes for `s01.melody.a`, `s01.keys.a`, and `s01.bass.a` with `simple-synth-1.0.0`. Tempo authority is the encoded microsecond value in the MIDI, 769231 us per quarter note. Sample positions use `floor(seconds * 44100 + 0.5)` from tick 0. Intervals are not summed. Sample-exact repeating loops at an arbitrary BPM are not promised.

The synth mapping is a sine plus a quiet triangle for the melody, a quiet triangle for the keys reference, and a sine for the bass. No program changes are encoded. A conventional GM player will normally use its default piano program for pitched channels unless configured otherwise; compatible GM channel 10 percussion is treated separately. Player behavior may vary. The mapping is not encoded in the MIDI. The renderer adds no noise.

Encoded MP3 settings: libmp3lame, 192 kbps. Film audio is AAC at 160 kbps re-encoded from that MP3, so the decoded film audio is not byte-identical to the MP3. Film duration probe: 24.615 seconds. MP3 container probe 24.615 seconds. MP4 probe 24.615 seconds. The film ends on a video frame, so it is slightly shorter than the MP3 container. The music is the same preview, not a different excerpt. The picture is a still illustration with rasterized disclosure text. DejaVu Sans Bold from the build machine supplies the glyphs. The font file is not in this pack.

No human listening audition was performed for this build. A sample peak is recorded in the preview manifest. It is not LUFS and it is not a true peak.

## Build

From the repository root, with Python 3.11+ and ffmpeg (libmp3lame, aac, libx264):

```bash
python3 tools/build_pack.py
python3 -m http.server 43181
```

The page is static. It is served with Python's HTTP server so the MIDI and media keep working relative paths. There is no application server and no package install. Standard library only.

`build/` holds the intermediate WAV, the procedural PPM, and the film plate. Those files are gitignored. The delivered audio is the MP3.

## Checks the validator actually runs

File existence, parse, PPQ, tempo, 4/4, end-of-track boundary, note pairing, ranges, monophonic melody, monophonic bass, keys polyphony cap of four, note-off before note-on at a shared tick, absence of program changes and other channel messages, departure flags only when a pitch leaves the declared pitch-class set, agreement with the canonical score, and agreement between `arrangement.mid` and the three source files. A negative overlap fixture is written outside the pack and must be rejected.

## Drafts and publication

Social captions, the X post, and the Medium article are drafts. They are not access controls. If this repository is public, the drafts are public. Do not treat them as posted to Instagram, X, or Medium.

Prepared repository description: Original note-only MIDI studies of chillhop melodies, with matched validation and a simple-synth preview.

Prepared topics: midi, chillhop, melody, music-production, composition.

No release tag was created. `index.html` keeps its name because players and links depend on it. This page is the file catalog the pack requires. GitHub Pages serves the gh-pages branch.

## Limitations

Variation compatibility is per study and is written on the page. Variation A and variation B of a study are alternatives. Pair keys A and bass A with melody A, and the B references with melody B. The arrangement is only study 01. Stacking it with the part files doubles those notes. These melodies are original. They are not house riffs and they are not jazz walks.
