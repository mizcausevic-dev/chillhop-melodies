"""Procedural raster artwork and ffmpeg media steps.

The painter is original and deterministic. It draws a dusk sky and a short
melody of bars with gaps between them. Amber marks the answer. It is an
illustration, not a photograph of a session or of performers.

DejaVu Sans Bold is used only to rasterize the disclosure into the film and the
poster. The font file is not shipped.
"""

from __future__ import annotations

import subprocess
from pathlib import Path

FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
ON_PICTURE = "preview, not master"


def _clamp(value: int) -> int:
    return 0 if value < 0 else 255 if value > 255 else value


def paint(width: int, height: int, framing: str) -> bytes:
    # Eight bars. Each bar is a short motif plus a gap, so the accompaniment has room.
    motifs = (
        (0.18, 0.34, 0.62),
        (0.22, 0.40),
        (0.16, 0.30, 0.48),
        (0.28,),
        (0.46, 0.72, 0.88),
        (0.55, 0.78),
        (0.24,),
        (0.36, 1.00),
    )
    margin_x = int(width * (0.08 if framing == "wide" else 0.1))
    horizon = int(height * (0.72 if framing == "square" else 0.68))
    sky_top = int(height * 0.08)
    span = max(1, width - margin_x * 2)
    cell = span / len(motifs)
    pixels = bytearray(width * height * 3)
    for y in range(height):
        shade = y / max(1, height - 1)
        if y < horizon:
            lift = y / max(1, horizon)
            red = int(42 + 150 * lift)
            green = int(28 + 92 * lift)
            blue = int(48 + 28 * lift)
        else:
            below = (y - horizon) / max(1, height - horizon)
            red = int(58 - 18 * below)
            green = int(36 - 10 * below)
            blue = int(28 - 8 * below)
        row = y * width * 3
        for x in range(width):
            pixels[row + x * 3] = _clamp(red)
            pixels[row + x * 3 + 1] = _clamp(green)
            pixels[row + x * 3 + 2] = _clamp(blue)
    for bar_index, levels in enumerate(motifs):
        inner = cell * 0.72
        note_w = inner / max(1, len(levels))
        for note_index, level in enumerate(levels):
            x0 = int(margin_x + bar_index * cell + note_index * note_w + note_w * 0.18)
            x1 = int(margin_x + bar_index * cell + note_index * note_w + note_w * 0.78)
            y0 = int(horizon - level * (horizon - sky_top))
            answer = level >= 0.86
            for y in range(max(0, y0), horizon):
                mix = (y - y0) / max(1, horizon - y0)
                if answer:
                    red, green, blue = 242, int(168 + 30 * mix), int(74 + 20 * mix)
                else:
                    red = int(214 - 30 * mix)
                    green = int(164 - 24 * mix)
                    blue = int(112 - 16 * mix)
                row = y * width * 3
                for x in range(max(0, x0), min(width, x1)):
                    pixels[row + x * 3] = _clamp(red)
                    pixels[row + x * 3 + 1] = _clamp(green)
                    pixels[row + x * 3 + 2] = _clamp(blue)
    return bytes(pixels)

def write_ppm(path: Path, width: int, height: int, rgb: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    header = f"P6\n{width} {height}\n255\n".encode("ascii")
    path.write_bytes(header + rgb)


def run(command: list[str]) -> None:
    completed = subprocess.run(command, check=False, capture_output=True, text=True)
    if completed.returncode != 0:
        raise RuntimeError(
            "command failed\n"
            + " ".join(command)
            + "\n"
            + completed.stderr[-2000:]
        )


def ppm_to_jpeg(ppm: Path, jpeg: Path, quality: int = 3) -> None:
    jpeg.parent.mkdir(parents=True, exist_ok=True)
    run(["ffmpeg", "-y", "-i", str(ppm), "-frames:v", "1", "-q:v", str(quality), str(jpeg)])


def draw_disclosure(source: Path, dest: Path, textfile: Path) -> list[str]:
    dest.parent.mkdir(parents=True, exist_ok=True)
    textfile.write_text(ON_PICTURE + "\n", encoding="utf-8")
    command = [
        "ffmpeg", "-y", "-i", str(source),
        "-vf",
        (
            f"drawtext=textfile={textfile}:fontfile={FONT}:fontsize=48:"
            "fontcolor=white:x=(w-text_w)/2:y=h-100:box=1:boxcolor=black@0.68:boxborderw=22"
        ),
        "-frames:v", "1",
        "-q:v", "3",
        str(dest),
    ]
    run(command)
    return command


def encode_mp3(wav: Path, mp3: Path) -> list[str]:
    mp3.parent.mkdir(parents=True, exist_ok=True)
    command = [
        "ffmpeg", "-y", "-i", str(wav),
        "-codec:a", "libmp3lame", "-b:a", "192k",
        str(mp3),
    ]
    run(command)
    return command


def encode_film(plate: Path, mp3: Path, mp4: Path, textfile: Path, duration: str) -> list[str]:
    mp4.parent.mkdir(parents=True, exist_ok=True)
    textfile.write_text(ON_PICTURE + "\n", encoding="utf-8")
    command = [
        "ffmpeg", "-y",
        "-loop", "1", "-framerate", "24", "-i", str(plate),
        "-i", str(mp3),
        "-t", duration,
        "-vf",
        (
            "scale=1280:720,"
            f"drawtext=textfile={textfile}:fontfile={FONT}:fontsize=48:"
            "fontcolor=white:x=(w-text_w)/2:y=h-100:box=1:boxcolor=black@0.68:boxborderw=22"
        ),
        "-r", "24",
        "-c:v", "libx264", "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "160k",
        "-shortest",
        "-movflags", "+faststart",
        str(mp4),
    ]
    run(command)
    return command


def derive_social(hero: Path, square: Path, portrait: Path, card: Path) -> dict[str, list[str]]:
    portrait.parent.mkdir(parents=True, exist_ok=True)
    card.parent.mkdir(parents=True, exist_ok=True)
    portrait_cmd = [
        "ffmpeg", "-y", "-i", str(square),
        "-vf", "crop=864:1080:108:0,scale=1080:1350",
        "-q:v", "3",
        str(portrait),
    ]
    card_cmd = [
        "ffmpeg", "-y", "-i", str(hero),
        "-vf", "scale=1600:900",
        "-q:v", "3",
        str(card),
    ]
    run(portrait_cmd)
    run(card_cmd)
    return {"portrait": portrait_cmd, "card": card_cmd}
