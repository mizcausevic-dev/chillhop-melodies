"""Original chillhop melody studies.

Tempos, lengths, and collections are fixed before the notes. Every study is
8 bars. A 16-bar container at 70-95 BPM lasts about 40.4 seconds or more,
which is outside the preview window. The pocket is the written grid.
Offsets are 0. Random jitter is not groove. Tape dust is not encoded.
"""

from __future__ import annotations

from tools.midi_io import BAR_TICKS_4_4, PPQ, bpm_to_us, effective_bpm

GENERATOR_VERSION = "1.0.0"
PACK_ID = "chillhop-melodies"
PACK_NAME = "Chillhop Melodies"
BAR = BAR_TICKS_4_4

# (bar, offset, duration, pitch). Melody is monophonic and written by hand.
MELODY = {
    "s01": {
        "a": [
            (0, 240, 480, 74), (0, 960, 240, 77), (0, 1440, 720, 81),
            (1, 240, 480, 74), (1, 960, 240, 76), (1, 1440, 960, 79),
            (2, 240, 480, 72), (2, 960, 240, 74), (2, 1440, 720, 77),
            (3, 480, 720, 69),
            (4, 240, 720, 81), (4, 1200, 480, 83), (4, 1920, 960, 79),
            (5, 240, 720, 76), (5, 1440, 1440, 74),
            (6, 960, 480, 72),
            (7, 240, 480, 69), (7, 960, 1920, 62),
        ],
        "b": [
            (0, 0, 240, 69), (0, 480, 240, 72), (0, 1440, 480, 74),
            (1, 0, 240, 67), (1, 720, 360, 71), (1, 1680, 480, 74),
            (2, 0, 240, 65), (2, 960, 240, 69), (2, 1920, 480, 72),
            (3, 480, 240, 74), (3, 1440, 720, 77),
            (4, 0, 360, 76), (4, 960, 240, 74), (4, 1920, 480, 71),
            (5, 240, 240, 69), (5, 1200, 960, 65),
            (6, 0, 1440, 62),
            (7, 480, 240, 64), (7, 1440, 720, 67),
        ],
    },
    "s02": {
        "a": [
            (0, 1440, 480, 69), (0, 2160, 240, 72), (0, 2640, 720, 76),
            (1, 1440, 480, 69), (1, 2160, 240, 67), (1, 2880, 720, 64),
            (2, 960, 360, 72), (2, 1680, 480, 76), (2, 2400, 960, 79),
            (3, 1440, 1440, 81),
            (4, 480, 720, 76), (4, 1440, 480, 72), (4, 2160, 960, 69),
            (5, 1440, 240, 67), (5, 1920, 960, 64),
            (6, 0, 480, 72), (6, 1920, 480, 69),
            (7, 480, 240, 64), (7, 1440, 1680, 60),
        ],
        "b": [
            (0, 0, 960, 81), (0, 1440, 480, 76), (0, 2400, 720, 72),
            (1, 480, 720, 76), (1, 1680, 480, 74), (1, 2640, 480, 71),
            (2, 0, 1440, 69), (2, 1920, 480, 67), (2, 2880, 480, 64),
            (3, 240, 1920, 62),
            (4, 0, 480, 64), (4, 960, 480, 67), (4, 1920, 960, 72),
            (5, 0, 240, 76), (5, 720, 1440, 69),
            (6, 960, 240, 65), (6, 1920, 720, 60),
            (7, 0, 480, 57), (7, 1440, 480, 60), (7, 2400, 960, 64),
        ],
    },
    "s03": {
        "a": [
            (0, 0, 1440, 65), (0, 1920, 240, 69), (0, 2400, 240, 72), (0, 2880, 720, 77),
            (1, 480, 1920, 74),
            (2, 0, 960, 72), (2, 1440, 480, 69), (2, 2400, 960, 65),
            (3, 960, 1440, 62),
            (4, 0, 720, 77), (4, 1200, 480, 76), (4, 2160, 1200, 72),
            (5, 240, 480, 69), (5, 1440, 1680, 65),
            (6, 1920, 960, 64),
            (7, 0, 480, 65), (7, 960, 2400, 60),
        ],
        "b": [
            (0, 720, 240, 70), (0, 1200, 240, 69), (0, 1920, 360, 65),
            (1, 480, 240, 67), (1, 1200, 480, 70), (1, 2160, 240, 74),
            (2, 240, 360, 77), (2, 960, 240, 74), (2, 1680, 480, 70),
            (3, 1440, 240, 65), (3, 2160, 720, 62),
            (4, 480, 240, 69), (4, 1200, 240, 72), (4, 1920, 480, 77),
            (5, 0, 360, 81), (5, 960, 240, 77), (5, 1680, 720, 74),
            (6, 720, 960, 70),
            (7, 240, 240, 65), (7, 960, 240, 62), (7, 1680, 480, 58),
        ],
    },
    "s04": {
        "a": [
            (0, 0, 480, 67), (0, 960, 240, 74), (0, 1920, 480, 72),
            (1, 480, 480, 71), (1, 1440, 720, 67),
            (2, 0, 360, 74), (2, 720, 240, 76), (2, 1440, 960, 79),
            (3, 960, 480, 74), (3, 1920, 960, 71),
            (4, 240, 720, 79), (4, 1440, 240, 76), (4, 2160, 720, 72),
            (5, 0, 1440, 67), (5, 2400, 480, 64),
            (6, 1440, 480, 62),
            (7, 0, 240, 67), (7, 720, 240, 71), (7, 1440, 1440, 74),
        ],
        "b": [
            (0, 240, 240, 79), (0, 720, 480, 76), (0, 1680, 360, 74),
            (1, 0, 960, 72), (1, 1440, 240, 71), (1, 2160, 720, 67),
            (2, 480, 240, 64), (2, 1200, 480, 67), (2, 2160, 960, 71),
            (3, 0, 480, 74), (3, 960, 240, 77), (3, 1680, 720, 74),
            (4, 720, 360, 76), (4, 1440, 480, 79), (4, 2400, 720, 83),
            (5, 240, 1440, 81),
            (6, 480, 240, 78), (6, 1200, 960, 79),
            (7, 0, 720, 71), (7, 1200, 480, 67), (7, 2160, 960, 62),
        ],
    },
    "s05": {
        "a": [
            (0, 0, 480, 72), (0, 720, 360, 76), (0, 1320, 480, 79),
            (1, 240, 720, 81), (1, 1440, 360, 76),
            (2, 0, 480, 74), (2, 720, 360, 77), (2, 1320, 480, 72),
            (3, 960, 1440, 67),
            (4, 0, 240, 76), (4, 480, 480, 79), (4, 1440, 240, 83), (4, 2160, 720, 81),
            (5, 480, 1920, 77),
            (6, 1440, 240, 74), (6, 2160, 480, 72),
            (7, 0, 960, 67), (7, 1920, 1440, 64),
        ],
        "b": [
            (0, 960, 240, 64), (0, 1440, 240, 67), (0, 2160, 480, 71),
            (1, 0, 360, 72), (1, 720, 240, 76), (1, 1440, 240, 74), (1, 2160, 720, 71),
            (2, 480, 240, 69), (2, 1200, 480, 65), (2, 2160, 480, 62),
            (3, 0, 240, 64), (3, 720, 1440, 60),
            (4, 240, 360, 67), (4, 960, 240, 71), (4, 1680, 480, 74),
            (5, 0, 480, 77), (5, 960, 240, 76), (5, 1680, 960, 72),
            (6, 720, 240, 69), (6, 1440, 720, 65),
            (7, 240, 240, 64), (7, 960, 480, 60), (7, 1920, 480, 55),
        ],
    },
    "s06": {
        "a": [
            (0, 0, 240, 64), (0, 480, 240, 66), (0, 960, 720, 71), (0, 2160, 960, 76),
            (1, 480, 480, 74), (1, 1440, 1440, 71),
            (2, 0, 240, 67), (2, 480, 240, 69), (2, 960, 480, 72), (2, 1920, 960, 76),
            (3, 240, 1920, 64),
            (4, 0, 360, 76), (4, 720, 240, 79), (4, 1440, 480, 83), (4, 2400, 960, 81),
            (5, 480, 720, 78), (5, 1680, 1200, 76),
            (6, 960, 480, 71),
            (7, 0, 480, 69), (7, 960, 240, 67), (7, 1680, 1440, 64),
        ],
        "b": [
            (0, 240, 720, 76), (0, 1440, 480, 74), (0, 2400, 720, 71),
            (1, 0, 960, 69), (1, 1440, 720, 67), (1, 2640, 720, 64),
            (2, 480, 240, 66), (2, 1200, 480, 64), (2, 2160, 960, 62),
            (3, 0, 1440, 60), (3, 1920, 480, 64),
            (4, 720, 240, 71), (4, 1440, 480, 74), (4, 2400, 720, 78),
            (5, 240, 360, 73), (5, 1200, 1440, 76),
            (6, 0, 480, 71), (6, 1440, 960, 67),
            (7, 480, 240, 64), (7, 1200, 480, 66), (7, 2160, 960, 71),
        ],
    },
    "s07": {
        "a": [
            (0, 0, 1440, 70), (0, 1920, 1440, 74),
            (1, 480, 1920, 77),
            (2, 0, 960, 75), (2, 1440, 480, 74), (2, 2400, 960, 70),
            (3, 960, 1920, 67),
            (4, 0, 240, 70), (4, 480, 240, 72), (4, 960, 1440, 75),
            (5, 0, 720, 79), (5, 1200, 1680, 77),
            (6, 1440, 960, 74),
            (7, 0, 480, 72), (7, 960, 2400, 70),
        ],
        "b": [
            (0, 480, 240, 69), (0, 960, 240, 70), (0, 1440, 480, 74), (0, 2400, 480, 77),
            (1, 240, 360, 75), (1, 960, 240, 74), (1, 1680, 720, 72),
            (2, 0, 240, 70), (2, 720, 240, 67), (2, 1440, 480, 65), (2, 2400, 480, 62),
            (3, 480, 1440, 58),
            (4, 720, 240, 63), (4, 1200, 240, 65), (4, 1920, 960, 70),
            (5, 0, 480, 74), (5, 960, 240, 77), (5, 1680, 480, 82),
            (6, 240, 720, 79), (6, 1440, 480, 75),
            (7, 480, 240, 72), (7, 1200, 240, 70), (7, 1920, 960, 65),
        ],
    },
    "s08": {
        "a": [
            (0, 0, 480, 71), (0, 1920, 960, 78),
            (1, 480, 360, 76), (1, 2160, 720, 74),
            (2, 0, 240, 73), (2, 960, 480, 71), (2, 2400, 720, 66),
            (3, 1440, 1440, 62),
            (4, 0, 240, 71), (4, 480, 240, 73), (4, 960, 480, 78), (4, 1920, 960, 83),
            (5, 240, 720, 81), (5, 1440, 480, 78), (5, 2400, 960, 74),
            (6, 960, 240, 71),
            (7, 0, 360, 66), (7, 960, 1920, 59),
        ],
        "b": [
            (0, 240, 240, 83), (0, 720, 480, 81), (0, 1680, 240, 78), (0, 2400, 720, 74),
            (1, 0, 480, 73), (1, 960, 240, 71), (1, 1680, 960, 69),
            (2, 480, 720, 66), (2, 1680, 240, 64), (2, 2400, 480, 62),
            (3, 0, 1440, 59),
            (4, 720, 240, 62), (4, 1440, 360, 66), (4, 2160, 720, 71),
            (5, 0, 240, 68), (5, 720, 960, 71),
            (6, 240, 480, 74), (6, 1440, 720, 78),
            (7, 0, 240, 81), (7, 720, 240, 78), (7, 1440, 1440, 71),
        ],
    },
}

# Planned true departures. Anything else outside a collection is an error.
PLANNED = {("s04", "b", 78), ("s06", "b", 73), ("s08", "b", 68)}


class Part:
    def __init__(self, study, part_id, role, variation, core, channel, slug, mono, poly, lo, hi):
        self.study = study
        self.part_id = part_id
        self.role = role
        self.variation = variation
        self.core = core
        self.channel = channel
        self.file_slug = slug
        self.monophonic = mono
        self.max_poly = poly
        self.lo = lo
        self.hi = hi
        self.container_ticks = study["bars"] * BAR
        self.notes = []

    def add(self, start, duration, pitch, velocity):
        end = start + duration
        if start < 0 or duration <= 0 or end > self.container_ticks:
            raise ValueError(f"{self.part_id} boundary {start}+{duration}")
        if not self.lo <= pitch <= self.hi:
            raise ValueError(f"{self.part_id} pitch {pitch}")
        if not 1 <= velocity <= 127:
            raise ValueError(f"{self.part_id} velocity {velocity}")
        pool = set(self.study["pitch_classes"])
        departure = (pitch % 12) not in pool
        active = 1
        for other in self.notes:
            o0 = other["performed_start"]
            o1 = o0 + other["duration"]
            if start < o1 and o0 < end:
                if other["pitch"] == pitch or self.monophonic:
                    raise ValueError(f"{self.part_id} overlap {pitch}@{start}")
                active += 1
        if active > self.max_poly:
            raise ValueError(f"{self.part_id} poly {active}")
        self.notes.append({
            "nominal_start": start, "offset": 0, "performed_start": start,
            "duration": duration, "pitch": pitch, "velocity": velocity,
            "channel": self.channel, "departure": departure,
        })

    def finish(self):
        ordered = sorted(self.notes, key=lambda n: (n["performed_start"], n["pitch"]))
        if self.core and len(ordered) < 8:
            raise ValueError(f"{self.part_id} too few notes")
        if not ordered:
            raise ValueError(f"{self.part_id} empty")
        for index, note in enumerate(ordered, 1):
            note["id"] = f"{self.part_id}.n{index:04d}"
        return {
            "id": self.part_id, "study_id": self.study["id"], "slug": self.study["slug"],
            "role": self.role, "variation": self.variation, "core": self.core,
            "channel": self.channel, "file_slug": self.file_slug,
            "path": f"midi/{self.study['slug']}/{self.file_slug}.mid",
            "monophonic": self.monophonic, "max_poly": self.max_poly,
            "container_ticks": self.container_ticks, "container_bars": self.study["bars"],
            "bpm": self.study["bpm"], "tempo_us": self.study["tempo_us"], "notes": ordered,
        }


def melody(study, variation):
    return Part(study, f"{study['id']}.melody.{variation}", "melody", variation, True, 0, f"melody-{variation}", True, 1, 55, 86)


def keys(study, variation):
    return Part(study, f"{study['id']}.keys.{variation}", "keys-reference", variation, False, 1, f"keys-{variation}", False, 4, 40, 76)


def bass(study, variation):
    return Part(study, f"{study['id']}.bass.{variation}", "bass-reference", variation, False, 2, f"bass-{variation}", True, 1, 28, 52)


def melody_velocity(bar_index):
    return (78, 78, 84, 84, 90, 96, 88, 104)[bar_index]


def place_melody(part, events):
    for bar_index, offset, duration, pitch in events:
        part.add(bar_index * BAR + offset, duration, pitch, melody_velocity(bar_index))


def chord_fifth(root, pool):
    for candidate in (root + 7, root - 5, root + 7 - 12):
        if 28 <= candidate <= 52 and (candidate % 12) in pool and candidate != root:
            return candidate
    return root


def place_keys(part, regions):
    for region in regions:
        b_pitches = None
        if len(region) == 4:
            start, length, pitches, b_pitches = region
        else:
            start, length, pitches = region
        if part.variation == "a":
            duration = length * BAR - 480
            for pitch in pitches:
                part.add(start * BAR, duration, pitch, 62)
        else:
            use = pitches[:3] if b_pitches is None else b_pitches
            for bar_index in range(start, start + length):
                for pitch in use:
                    part.add(bar_index * BAR + 960, 960, pitch, 54)


def place_bass(part, roots):
    pool = set(part.study["pitch_classes"])
    study_id = part.study["id"]
    for start, length, root in roots:
        for bar_index in range(start, start + length):
            if part.variation == "a" and study_id == "s06":
                upper = chord_fifth(root, pool)
                part.add(bar_index * BAR + 960, 480, root, 74)
                part.add(bar_index * BAR + 1920, 240, upper, 90)
                part.add(bar_index * BAR + 2880, 720, root, 60)
            elif part.variation == "a" and study_id == "s07":
                upper = chord_fifth(root, pool)
                part.add(bar_index * BAR, 1440, root, 72)
                part.add(bar_index * BAR + 2400, 960, upper, 80)
            elif part.variation == "a":
                part.add(bar_index * BAR, 720, root, 86)
                part.add(bar_index * BAR + 1920, 480, root, 68)
            else:
                upper = chord_fifth(root, pool)
                part.add(bar_index * BAR + 480, 960, root, 80)
                part.add(bar_index * BAR + 2880, 360, upper, 64)


def studies():
    common = {"meter": "4/4", "bar_ticks": BAR, "ppq": PPQ, "stochastic_draws": 0, "bars": 8}
    rows = [
        {**common, "id": "s01", "slug": "s01-second-sixteenth", "title": "Second Sixteenth", "bpm": 78,
         "tonic": "D", "tonal_reference": "D", "collection_name": "D dorian",
         "pitch_classes": [0, 2, 4, 5, 7, 9, 11], "seed": 7801,
         "harmonic_rhythm": "Four bars of Dm7, two of G, two of Dm7.",
         "changes": ["Dm7", "G", "Dm7"], "change_bars": [4, 2, 2],
         "phrases": [
             {"name": "Late call", "start_bar": 0, "bars": 2},
             {"name": "Reply", "start_bar": 2, "bars": 2},
             {"name": "Answer", "start_bar": 4, "bars": 2},
             {"name": "Landing", "start_bar": 6, "bars": 2},
         ],
         "identity": "The call starts a sixteenth late. Bar 2 tops a minor third lower, at G5. The later answer starts a fifth higher, on A5. Variation B moves onto the downbeat, shortens the attacks, and sits lower.",
         "limitations": "Pair melody A with keys A and bass A. The late sixteenth is the pocket. It is not a random offset.",
         "voicing": "Melody is one note at a time, from D4 up to B5. Keys A is Dm7: D, F, A, C. Keys B on those bars keeps D, F, and C.",
         "layering": "Keys and bass are reference files. They are not written into the melody file.",
         "accent": "Velocity steps 78, 78, 84, 84, 90, 96, 88, 104 across the eight bars.",
         "keys": [(0, 4, [50, 57, 60, 65], [50, 65, 60]), (4, 2, [55, 59, 62, 67]), (6, 2, [50, 57, 60, 65], [50, 65, 60])],
         "bass": [(0, 4, 38), (4, 2, 43), (6, 2, 38)]},
        {**common, "id": "s02", "slug": "s02-and-of-two", "title": "And of Two", "bpm": 84,
         "tonic": "A", "tonal_reference": "A", "collection_name": "A natural minor",
         "pitch_classes": [0, 2, 4, 5, 7, 9, 11], "seed": 8402,
         "harmonic_rhythm": "Two bars each: Am, F, C, Am.",
         "changes": ["Am", "F", "C", "Am"], "change_bars": [2, 2, 2, 2],
         "phrases": [
             {"name": "Wait", "start_bar": 0, "bars": 2},
             {"name": "Rise", "start_bar": 2, "bars": 2},
             {"name": "Turn", "start_bar": 4, "bars": 2},
             {"name": "Low answer", "start_bar": 6, "bars": 2},
         ],
         "identity": "The motif waits until the and of two, then gives a short answer. Variation B starts on the downbeat with longer notes and a higher first pitch.",
         "limitations": "The empty first half of bars 1 and 2 is space for the keys reference, not a missing file.",
         "voicing": "Melody stays monophonic between A3 and A5.",
         "layering": "The F and C colors live in the keys reference, not in the melody file.",
         "accent": "The same eight-bar velocity ladder as the other studies.",
         "keys": [(0, 2, [45, 52, 60, 64]), (2, 2, [53, 60, 65, 69]), (4, 2, [48, 55, 60, 64]), (6, 2, [45, 52, 60, 64])],
         "bass": [(0, 2, 33), (2, 2, 41), (4, 2, 36), (6, 2, 33)]},
        {**common, "id": "s03", "slug": "s03-held-answer", "title": "Held Answer", "bpm": 72,
         "tonic": "F", "tonal_reference": "F", "collection_name": "F major",
         "pitch_classes": [0, 2, 4, 5, 7, 9, 10], "seed": 7203,
         "harmonic_rhythm": "Two bars each: F, Bb, C, F.",
         "changes": ["F", "Bb", "C", "F"], "change_bars": [2, 2, 2, 2],
         "phrases": [
             {"name": "Hold", "start_bar": 0, "bars": 2},
             {"name": "Reply", "start_bar": 2, "bars": 2},
             {"name": "Color", "start_bar": 4, "bars": 2},
             {"name": "Cadence", "start_bar": 6, "bars": 2},
         ],
         "identity": "A held tone gives way to a three-note answer. Variation B never holds. It uses short notes and leans on Bb.",
         "limitations": "The long notes are written durations. Release tails are not extra notes.",
         "voicing": "Melody is monophonic from Bb3 to A5. Keys hold a close shell.",
         "layering": "The held keys chord is a reference. It does not share the melody file.",
         "accent": "The cadence bar is louder than the held call.",
         "keys": [(0, 2, [53, 60, 65, 69]), (2, 2, [58, 65, 70, 74]), (4, 2, [55, 60, 64, 67]), (6, 2, [53, 60, 65, 69])],
         "bass": [(0, 2, 41), (2, 2, 46), (4, 2, 48), (6, 2, 41)]},
        {**common, "id": "s04", "slug": "s04-fifth-then-rest", "title": "Fifth Then Rest", "bpm": 90,
         "tonic": "G", "tonal_reference": "G", "collection_name": "G mixolydian",
         "pitch_classes": [0, 2, 4, 5, 7, 9, 11], "seed": 9004,
         "harmonic_rhythm": "Two bars each: G, C, F, G.",
         "changes": ["G", "C", "F", "G"], "change_bars": [2, 2, 2, 2],
         "phrases": [
             {"name": "Leap", "start_bar": 0, "bars": 2},
             {"name": "Neighbor", "start_bar": 2, "bars": 2},
             {"name": "Fall", "start_bar": 4, "bars": 2},
             {"name": "Close", "start_bar": 6, "bars": 2},
         ],
         "identity": "A fifth leap, a rest, then a neighbor. Variation B compresses the leap and uses one flagged F#5.",
         "limitations": "F#5 is outside G mixolydian. It is one sixteenth in variation B, then the line returns to G.",
         "voicing": "Melody is monophonic. The fifth is a melodic leap, not a keys voicing.",
         "layering": "F and C are keys-reference chords. The melody does not carry those shells.",
         "accent": "The leap is mid velocity. The last bar of variation A is the peak.",
         "keys": [(0, 2, [55, 62, 67, 71]), (2, 2, [60, 64, 67, 72]), (4, 2, [53, 60, 65, 69]), (6, 2, [55, 62, 67, 71])],
         "bass": [(0, 2, 43), (2, 2, 48), (4, 2, 41), (6, 2, 43)]},
        {**common, "id": "s05", "slug": "s05-question-rest", "title": "Question Rest", "bpm": 76,
         "tonic": "C", "tonal_reference": "C", "collection_name": "C major",
         "pitch_classes": [0, 2, 4, 5, 7, 9, 11], "seed": 7605,
         "harmonic_rhythm": "Two bars each: C, Am, F, G.",
         "changes": ["C", "Am", "F", "G"], "change_bars": [2, 2, 2, 2],
         "phrases": [
             {"name": "Question", "start_bar": 0, "bars": 2},
             {"name": "Empty", "start_bar": 2, "bars": 2},
             {"name": "Answer", "start_bar": 4, "bars": 2},
             {"name": "Settle", "start_bar": 6, "bars": 2},
         ],
         "identity": "The question occupies the first half of the bar and leaves the rest empty. Variation B fills that empty half with a different contour.",
         "limitations": "The empty beats are intentional space. They are not dropped events.",
         "voicing": "Melody is monophonic from G3 to B5.",
         "layering": "Am and F are reference chords under the rests.",
         "accent": "The answer bars sit higher in the velocity ladder than the question.",
         "keys": [(0, 2, [60, 64, 67, 72]), (2, 2, [57, 64, 69, 72]), (4, 2, [53, 60, 65, 69]), (6, 2, [55, 59, 62, 67])],
         "bass": [(0, 2, 36), (2, 2, 33), (4, 2, 41), (6, 2, 43)]},
        {**common, "id": "s06", "slug": "s06-step-and-leap", "title": "Step and Leap", "bpm": 86,
         "tonic": "E", "tonal_reference": "E", "collection_name": "E natural minor",
         "pitch_classes": [0, 2, 4, 6, 7, 9, 11], "seed": 8606,
         "harmonic_rhythm": "Two bars each: Em, C, G, Em.",
         "changes": ["Em", "C", "G", "Em"], "change_bars": [2, 2, 2, 2],
         "phrases": [
             {"name": "Steps", "start_bar": 0, "bars": 2},
             {"name": "Leap", "start_bar": 2, "bars": 2},
             {"name": "Hold", "start_bar": 4, "bars": 2},
             {"name": "Return", "start_bar": 6, "bars": 2},
         ],
         "identity": "Steps lead to a leap and a hold. Variation B uses longer offbeat notes and one flagged C#5.",
         "limitations": "C#5 is outside E natural minor. It is one short note in variation B.",
         "voicing": "Melody is monophonic. The leap is a single interval, not a chord.",
         "layering": "The C and G references enter while the melody holds or rests.",
         "accent": "The held answer is louder than the opening steps.",
         "keys": [(0, 2, [52, 59, 64, 71]), (2, 2, [60, 64, 67, 72]), (4, 2, [55, 59, 62, 67]), (6, 2, [52, 59, 64, 71])],
         "bass": [(0, 2, 40), (2, 2, 48), (4, 2, 43), (6, 2, 40)]},
        {**common, "id": "s07", "slug": "s07-soft-cadence", "title": "Soft Cadence", "bpm": 70,
         "tonic": "Bb", "tonal_reference": "Bb", "collection_name": "Bb major",
         "pitch_classes": [0, 2, 3, 5, 7, 9, 10], "seed": 7007,
         "harmonic_rhythm": "Two bars each: Bb, Eb, F, Bb.",
         "changes": ["Bb", "Eb", "F", "Bb"], "change_bars": [2, 2, 2, 2],
         "phrases": [
             {"name": "Call", "start_bar": 0, "bars": 2},
             {"name": "Color", "start_bar": 2, "bars": 2},
             {"name": "Pickup", "start_bar": 4, "bars": 2},
             {"name": "Cadence", "start_bar": 6, "bars": 2},
         ],
         "identity": "The opening calls are dotted quarters at 70 BPM. Bar 2 is a half note. A three-note pickup happens only once. Variation B breaks those holds into short notes around A and C.",
         "limitations": "70 BPM is the slow end of this pack. The container is still 8 bars so the preview stays under 28 seconds.",
         "voicing": "Melody is monophonic from Bb3 to Bb5. Eb is a color tone, not a new key.",
         "layering": "The Eb and F shells are keys references.",
         "accent": "The pickup bar is the loudest stretch. The cadence eases off, then the last note peaks.",
         "keys": [(0, 2, [58, 65, 70, 74]), (2, 2, [63, 67, 70, 75]), (4, 2, [53, 60, 65, 69]), (6, 2, [58, 65, 70, 74])],
         "bass": [(0, 2, 34), (2, 2, 39), (4, 2, 41), (6, 2, 34)]},
        {**common, "id": "s08", "slug": "s08-open-space", "title": "Open Space", "bpm": 94,
         "tonic": "B", "tonal_reference": "B", "collection_name": "B natural minor",
         "pitch_classes": [1, 2, 4, 6, 7, 9, 11], "seed": 9408,
         "harmonic_rhythm": "Two bars each: Bm, G, A, Bm.",
         "changes": ["Bm", "G", "A", "Bm"], "change_bars": [2, 2, 2, 2],
         "phrases": [
             {"name": "Gap", "start_bar": 0, "bars": 2},
             {"name": "Single", "start_bar": 2, "bars": 2},
             {"name": "Answer", "start_bar": 4, "bars": 2},
             {"name": "Breath", "start_bar": 6, "bars": 2},
         ],
         "identity": "Two notes sit far apart, then one denser answer, then space. Variation B fills more of the bar and uses one flagged G#4.",
         "limitations": "G#4 is outside B natural minor. It is one note in variation B. 94 BPM is the fast end of this pack.",
         "voicing": "Melody is monophonic from B3 to B5, with wide gaps.",
         "layering": "G and A are reference chords in the gaps. They are not melody notes.",
         "accent": "The dense answer is louder than the isolated notes.",
         "keys": [(0, 2, [59, 66, 71, 74]), (2, 2, [55, 59, 62, 67]), (4, 2, [57, 61, 64, 69]), (6, 2, [59, 66, 71, 74])],
         "bass": [(0, 2, 35), (2, 2, 43), (4, 2, 45), (6, 2, 35)]},
    ]
    for row in rows:
        row["tempo_us"] = bpm_to_us(row["bpm"])
        row["effective_bpm"] = effective_bpm(row["tempo_us"])
        seconds = row["bars"] * 4 * 60 / row["bpm"]
        row["requested_seconds"] = seconds
        if not 70 <= row["bpm"] <= 95 or not isinstance(row["bpm"], int):
            raise ValueError(row["bpm"])
        if row["bars"] != 8:
            raise ValueError(row["id"])
        if not 10 < seconds < 38:
            raise ValueError(f"{row['id']} seconds {seconds}")
    return rows


def _sig(notes):
    return tuple((note["performed_start"], note["pitch"], note["duration"]) for note in notes)


def assert_identities(parts):
    melodies = [part for part in parts if part["role"] == "melody"]
    by = {}
    for part in melodies:
        by.setdefault(part["study_id"], {})[part["variation"]] = part
    seen = {}
    report = []
    for study_id, vars_ in by.items():
        notes_a = vars_["a"]["notes"]
        notes_b = vars_["b"]["notes"]
        sig_a = _sig(notes_a)
        if sig_a == _sig(notes_b):
            raise ValueError(f"{study_id} variations match")
        starts_a = tuple(note["performed_start"] for note in notes_a)
        starts_b = tuple(note["performed_start"] for note in notes_b)
        pitches_a = tuple(note["pitch"] for note in notes_a)
        pitches_b = tuple(note["pitch"] for note in notes_b)
        durations_a = tuple(note["duration"] for note in notes_a)
        durations_b = tuple(note["duration"] for note in notes_b)
        if starts_a == starts_b:
            raise ValueError(f"{study_id} variations share starts")
        if pitches_a == pitches_b:
            raise ValueError(f"{study_id} variations share pitches")
        if durations_a == durations_b:
            raise ValueError(f"{study_id} variations share durations")
        if sig_a in seen:
            raise ValueError(f"{study_id} attack tuples repeat {seen[sig_a]}")
        seen[sig_a] = study_id
        report.append({
            "study_id": study_id,
            "a": len(notes_a),
            "b": len(notes_b),
            "start_differs": True,
            "pitch_differs": True,
            "duration_differs": True,
        })
    if len(seen) != 8:
        raise ValueError("variation A attack tuples are not one per study")
    return {
        "studies": report,
        "method": "Melody A and melody B differ in start, pitch, and duration. Variation A attack tuples are unique across the eight studies.",
    }


def assert_no_transposed_bass(parts):
    bass = [part for part in parts if part["role"] == "bass-reference" and part["variation"] == "a"]
    seen = {}
    for part in bass:
        base = part["notes"][0]["pitch"]
        shape = tuple(
            (note["performed_start"], note["duration"], note["velocity"], note["pitch"] - base)
            for note in part["notes"]
        )
        if shape in seen:
            raise ValueError(f"{part['id']} copies {seen[shape]} at a constant interval")
        seen[shape] = part["id"]


def assert_departures(catalog_studies, parts):
    found = set()
    for part in parts:
        pool = set(next(study["pitch_classes"] for study in catalog_studies if study["id"] == part["study_id"]))
        for note in part["notes"]:
            inside = (note["pitch"] % 12) in pool
            if note["departure"] and inside:
                raise ValueError(f"{part['id']} flagged {note['pitch']} inside the collection")
            if not note["departure"] and not inside:
                raise ValueError(f"{part['id']} {note['pitch']} left the collection without a flag")
            if note["departure"]:
                key = (part["study_id"], part["variation"], note["pitch"])
                if key not in PLANNED:
                    raise ValueError(f"unplanned departure {key}")
                if part["role"] != "melody":
                    raise ValueError(f"departure on a reference part {part['id']}")
                found.add(key)
    if found != PLANNED:
        raise ValueError(f"departure set {found} != {PLANNED}")


def departure_lines(study, parts):
    lines = []
    for part in parts:
        if part["study_id"] != study["id"]:
            continue
        for note in part["notes"]:
            if note["departure"]:
                lines.append(
                    f"{part['id']} pitch {note['pitch']} is outside {study['collection_name']} and is flagged."
                )
    return lines


def build_study(study):
    built = []
    for variation in ("a", "b"):
        line = melody(study, variation)
        place_melody(line, MELODY[study["id"]][variation])
        chord = keys(study, variation)
        place_keys(chord, study["keys"])
        low = bass(study, variation)
        place_bass(low, study["bass"])
        built.extend([line.finish(), chord.finish(), low.finish()])
    return built


def compose():
    catalog_studies = studies()
    parts = []
    for study in catalog_studies:
        parts.extend(build_study(study))
    assert_departures(catalog_studies, parts)
    assert_no_transposed_bass(parts)
    identity = assert_identities(parts)
    for study in catalog_studies:
        study["departures"] = departure_lines(study, parts)
    core = [part for part in parts if part["core"]]
    refs = [part for part in parts if not part["core"]]
    if len(core) != 16 or len(refs) != 32:
        raise ValueError((len(core), len(refs)))
    if any(part["role"] != "melody" for part in core):
        raise ValueError("core role drifted")
    preview = next(study for study in catalog_studies if study["id"] == "s01")
    arrangement = {
        "id": "arrangement-preview-s01a",
        "path": "midi/arrangement.mid",
        "format": 1,
        "container_ticks": preview["bars"] * BAR,
        "bpm": preview["bpm"],
        "tempo_us": preview["tempo_us"],
        "meter": "4/4",
        "description": "Study 01 variation A melody with keys reference A and bass reference A. The references are not inside the melody file.",
        "tracks": [
            {"name": "Conductor", "source_part": None, "channel": None},
            {"name": "Melody", "source_part": "s01.melody.a", "channel": 0},
            {"name": "Keys Reference", "source_part": "s01.keys.a", "channel": 1},
            {"name": "Bass Reference", "source_part": "s01.bass.a", "channel": 2},
        ],
    }
    catalog = {
        "pack_id": PACK_ID, "pack_name": PACK_NAME,
        "catalog_version": GENERATOR_VERSION, "generator_version": GENERATOR_VERSION,
        "ppq": PPQ, "meter": {"numerator": 4, "denominator": 4, "bar_ticks": BAR},
        "pitched_range": [28, 86], "c4": 60,
        "note_policy": "Note-only MIDI. Pocket is the written grid. Offsets are 0. Random jitter, tape dust, and noise are not notes.",
        "microtiming": "offset is 0; performed_start = nominal_start",
        "stochastic_draws": 0,
        "seed_meaning": "Seeds identify studies. Nothing is random.",
        "container_choice": "Eight bars for every study. Sixteen bars at 70-95 BPM lasts about 40.4 seconds or longer.",
        "core_part_count": len(core), "reference_part_count": len(refs),
        "range_statement": "Melody is the core, monophonic, MIDI 55 to 86. Keys references use MIDI 40 to 76, at most four notes at once, and are not core. Bass references are monophonic, MIDI 28 to 52, and are not core.",
        "studies": [{key: study[key] for key in (
            "id", "slug", "title", "bpm", "tempo_us", "effective_bpm", "bars", "meter", "bar_ticks",
            "tonic", "tonal_reference", "collection_name", "pitch_classes", "departures", "seed",
            "harmonic_rhythm", "changes", "change_bars", "phrases", "identity", "limitations",
            "voicing", "layering", "accent", "stochastic_draws", "requested_seconds",
        )} for study in catalog_studies],
        "parts": [{
            "id": part["id"], "study_id": part["study_id"], "role": part["role"], "variation": part["variation"],
            "core": part["core"], "channel": part["channel"], "path": part["path"], "notes": len(part["notes"]),
            "container_bars": part["container_bars"], "bpm": part["bpm"], "monophonic": part["monophonic"],
        } for part in parts],
        "arrangement": arrangement,
        "preview_part_ids": ["s01.melody.a", "s01.keys.a", "s01.bass.a"],
        "stack_warning": "Use either the combined arrangement or the separate parts. Do not stack the part files on top of the combined file.",
    }
    score = {
        "pack_id": PACK_ID, "generator_version": GENERATOR_VERSION, "ppq": PPQ,
        "parts": parts, "arrangement": arrangement, "identity_check": identity,
    }
    return {"catalog": catalog, "score": score}
