"""Factual article draft. Not published."""

from __future__ import annotations

from tools.statements import AUDITION, ON_PICTURE, PREVIEW_LINE, PROGRAM, PUBLICATION, WARNING

TITLE = "Chillhop Melodies is a note-only MIDI study pack"
SUBTITLE = "Eight short motifs, a matched byte check, and a simple-synth preview that is not a master"
TAGS = ["midi", "chillhop", "melody", "music-production", "composition"]
TAG_LINE = "Tags: " + ", ".join(TAGS)

PARAGRAPHS = [
    "DRAFT. " + PUBLICATION,
    TAG_LINE,
    "The pack is eight melody studies in 4/4. Tempos sit between 70 and 95 BPM. Every study is 8 bars, chosen before the notes. Sixteen bars at those tempos would run past 40 seconds, so the container stays at 8. Each study has two melody variations. That is the core: sixteen files. Each study also has two keys references and two bass references. Those thirty-two files are not part of the core count, and they are not merged into the melody files.",
    "A variation has to change the melody in start, pitch, and duration. Second Sixteenth begins a sixteenth late and answers a third higher. And of Two waits until the and of two. Held Answer keeps a long tone, then a short reply. Fifth Then Rest leaps and leaves a gap. Question Rest empties the second half of the bar. Step and Leap climbs by step into a leap. Soft Cadence uses half notes at 70 BPM. Open Space places two notes far apart. Variation B of Fifth Then Rest, Step and Leap, and Open Space each contain one flagged pitch outside the collection. No other note is flagged.",
    "The pocket is the written grid. Offsets are 0. Random jitter is not groove, and tape dust is not a note. Melody notes stay between MIDI 55 and 86 and never overlap. Keys references stay between 40 and 76, with at most four notes sounding, and they are labeled reference. Bass stays between 28 and 52 and is monophonic. C4 is 60. The resolution is 960 ticks per quarter note. These melodies are original. They are not house riffs and they are not jazz walks.",
    PROGRAM,
    "Chorus, filters, tape, and sampler stacks are not in the files. The preview synth uses a sine plus a quiet triangle for the melody, a quiet triangle for the keys reference, and a sine for the bass. That mapping is documented. It is not a program change. The renderer adds no noise.",
    "The primary preview is study 01, Second Sixteenth, variation A, for all 8 bars: the melody file with keys reference A and bass reference A. At 78 BPM that container is 24.615 seconds by the bar formula. The other studies are in the MIDI and are not in that audio file. "
    + PREVIEW_LINE
    + ". The film takes its audio from that preview file and shows the words "
    + ON_PICTURE
    + " on the picture and in the WebVTT captions.",
    AUDITION
    + " The validator reopened the MIDI bytes and compared them with the canonical score. That is a structural check. The sample peak written beside the preview is the peak of the integer mix. It is not LUFS and it is not a true-peak reading. Nothing in this build is claimed as a master.",
    "The stills are procedural illustrations of a dusk melody with gaps between the bars. Amber marks the answer. They are not photographs of a session or of performers.",
    "When a public URL exists, use either the combined arrangement or the separate parts. " + WARNING,
    "Call to action: the MIDI, the matched report, and the preview belong together. Do not publish this draft to Medium, Instagram, or X from the draft files alone.",
]
if len(TAGS) > 5:
    raise RuntimeError("too many tags")


def markdown() -> str:
    body = "\n\n".join(PARAGRAPHS)
    return f"# {TITLE}\n\n{SUBTITLE}\n\n{body}\n"


def plain_text() -> str:
    lines = [TITLE, "", SUBTITLE, "", *PARAGRAPHS, ""]
    return "\n".join(lines) + "\n"
