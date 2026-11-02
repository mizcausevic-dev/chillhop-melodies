"""Catalog page. The melody roll is measured from the MIDI files.

Keys and bass stay in their own lanes. They are never drawn into the melody.
"""

from __future__ import annotations

import json
from pathlib import Path

from tools.screening import dusk_frames, render_media
from tools.statements import AUDITION, ON_PICTURE, PREVIEW_LINE, PROGRAM, PUBLICATION, WARNING

SPELL = {
    "s01": ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"],
    "s02": ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"],
    "s03": ["C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Bb", "B"],
    "s04": ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"],
    "s05": ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"],
    "s06": ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"],
    "s07": ["C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Bb", "B"],
    "s08": ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"],
}


def write_page(path: Path, catalog: dict, report: dict, preview: dict, film: dict) -> None:
    path.write_text(render_page(catalog, report, preview, film), encoding="utf-8")
    root = path.parent
    path.with_name("media.html").write_text(render_media({
        "pack_name": catalog["pack_name"],
        "subject": "The still is a dusk melody. Short bars leave gaps for an accompaniment. Amber marks the answer.",
        "colors": {
            "bg": "#241810",
            "paper": "#f6ead8",
            "ink": "#2c1a12",
            "accent": "#e28a3c",
            "muted": "#d9c4ae",
        },
        "frames": dusk_frames(root),
        "preview_seconds": preview["seconds_encoded"],
        "film_seconds": film["duration_seconds"],
    }), encoding="utf-8")


def render_page(catalog: dict, report: dict, preview: dict, film: dict) -> str:
    rows = []
    for part in catalog["parts"]:
        if part["core"]:
            kind = "core"
        elif part["role"] == "keys-reference":
            kind = "keys reference"
        else:
            kind = "bass reference"
        rows.append(
            "<tr>"
            f"<td><a href=\"{part['path']}\">{part['id']}</a></td>"
            f"<td>{part['role']}</td>"
            f"<td>{part['variation']}</td>"
            f"<td>{kind}</td>"
            f"<td>{part['bpm']}</td>"
            f"<td>{part['notes']}</td>"
            "</tr>"
        )
    set_map = []
    for study in catalog["studies"]:
        members = [part for part in catalog["parts"] if part["study_id"] == study["id"]]
        links = ", ".join(f"<a href=\"{part['path']}\">{part['id']}</a>" for part in members)
        set_map.append(f"<li><strong>{study['id']} {study['title']}</strong>: {links}</li>")
    payload = {
        "studies": [
            {
                "id": study["id"],
                "title": study["title"],
                "bpm": study["bpm"],
                "bars": study["bars"],
                "collection": study["collection_name"],
                "tonic": study["tonal_reference"],
                "identity": study["identity"],
                "limitations": study["limitations"],
                "voicing": study["voicing"],
                "layering": study["layering"],
                "accent": study["accent"],
                "departures": study["departures"],
                "harmonic_rhythm": study["harmonic_rhythm"],
                "changes": study["changes"],
                "change_bars": study["change_bars"],
                "phrases": study["phrases"],
                "tempo_us": study["tempo_us"],
                "seconds": study["requested_seconds"],
                "spell": SPELL[study["id"]],
            }
            for study in catalog["studies"]
        ],
        "parts": [
            {
                "id": part["id"],
                "study_id": part["study_id"],
                "role": part["role"],
                "variation": part["variation"],
                "path": part["path"],
                "core": part["core"],
            }
            for part in catalog["parts"]
        ],
    }
    data = json.dumps(payload, ensure_ascii=False).replace("<", "\\u003c")
    seconds = f"{preview['seconds_encoded']:.2f}"
    film_seconds = f"{film['duration_seconds']:.2f}"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Chillhop Melodies</title>
  <style>
    :root {{
      --bg: #241810;
      --paper: #f6ead8;
      --ink: #2c1a12;
      --amber: #e28a3c;
      --dusk: #8c4e3a;
      --gold: #f0c27a;
      --muted: #d9c4ae;
      --line: rgba(246, 234, 216, .16);
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0; background: var(--bg); color: var(--paper);
      font-family: Georgia, "Iowan Old Style", Palatino, serif;
      line-height: 1.45; padding-bottom: 28px;
    }}
    a {{ color: #f0c27a; }}
    button, .meta, .note, .transport {{ font-family: ui-monospace, Menlo, Consolas, monospace; }}
    .top {{
      position: sticky; top: 0; z-index: 6;
      display: flex; justify-content: space-between; gap: 12px; align-items: center;
      padding: 12px 20px; background: rgba(36, 24, 16, .94); border-bottom: 1px solid var(--line);
    }}
    .brand {{ letter-spacing: .14em; text-transform: uppercase; font-size: .72rem; }}
    .top nav {{ display: flex; gap: 14px; font-size: .78rem; }}
    main {{ width: min(1180px, calc(100% - 2rem)); margin: 0 auto; }}
    .stage {{
      display: grid; grid-template-columns: minmax(0, .8fr) minmax(0, 1.2fr);
      gap: 28px; align-items: start; padding: 26px 0 8px;
    }}
    .stage > div {{ min-width: 0; }}
    h1 {{ font-weight: 500; font-size: clamp(2.4rem, 5vw, 4.4rem); line-height: .92; margin: 8px 0 10px; }}
    h2 {{ font-weight: 500; }}
    .kicker {{ letter-spacing: .16em; text-transform: uppercase; color: var(--amber); font-size: .74rem; margin: 0; }}
    .meta, .note {{ color: var(--muted); font-size: .82rem; }}
    .hero img {{ display: block; width: 100%; height: auto; border-radius: 12px; }}
    .rail, .phrases, .switch {{ display: flex; gap: 8px; flex-wrap: wrap; margin: 8px 0; }}
    .rail {{ overflow-x: auto; flex-wrap: nowrap; max-width: 100%; padding-bottom: 4px; }}
    button {{
      border: 1px solid var(--line); background: transparent; color: var(--paper);
      border-radius: 999px; padding: 7px 11px; cursor: pointer;
    }}
    button[aria-pressed="true"] {{ background: var(--amber); color: #2c1a12; border-color: var(--amber); }}
    .scroller {{ overflow-x: auto; max-width: 100%; background: var(--paper); color: var(--ink); border-radius: 16px; padding: 8px 0 12px; }}
    .ruler, .lane {{ position: relative; }}
    .ruler {{ height: 28px; }}
    .change {{
      position: absolute; top: 4px; height: 20px; border-left: 2px solid var(--amber);
      padding-left: 5px; font-size: 11px; white-space: nowrap; overflow: hidden;
    }}
    .lane {{ height: 168px; border-top: 1px solid rgba(44, 26, 18, .12); }}
    .lane-label {{
      position: sticky; left: 8px; top: 4px; z-index: 2; display: inline-block;
      font-size: 10px; letter-spacing: .12em; text-transform: uppercase; color: #6d5344;
      background: var(--paper); padding: 0 4px;
    }}
    .block {{
      position: absolute; border-radius: 3px; min-width: 3px; background: var(--ink);
    }}
    .block.hot {{ background: var(--dusk); }}
    .phrase-band {{
      position: absolute; top: 22px; bottom: 0; background: rgba(226, 138, 60, .12); pointer-events: none;
    }}
    .keys-lane, .bass-lane {{
      height: 72px; background: #2c1a12; color: var(--paper); display: none; position: relative;
    }}
    .keys-lane.on, .bass-lane.on {{ display: block; }}
    .keys-lane .lane-label, .bass-lane .lane-label {{ color: var(--gold); background: transparent; }}
    .knote, .bnote {{
      position: absolute; height: 16px; border-radius: 3px; min-width: 3px;
    }}
    .knote {{ top: 36px; background: #e28a3c; }}
    .bnote {{ top: 40px; background: #f0c27a; }}
    .spark {{ display: flex; align-items: flex-end; gap: 2px; height: 46px; margin-top: 8px; }}
    .spark i {{ display: block; width: 4px; background: var(--amber); border-radius: 2px 2px 0 0; }}
    .legend {{ display: flex; gap: 14px; flex-wrap: wrap; font-size: .78rem; color: var(--muted); }}
    .swatch {{ display: inline-block; width: 10px; height: 10px; border-radius: 2px; margin-right: 4px; }}
    .table-scroll {{ overflow-x: auto; max-width: 100%; }}
    table {{ width: 100%; border-collapse: collapse; font-size: .8rem; }}
    th, td {{ text-align: left; padding: 7px 6px; border-bottom: 1px solid var(--line); }}
    .flow {{ display: flex; flex-wrap: wrap; gap: 8px; }}
    .flow span {{ border: 1px solid var(--line); border-radius: 999px; padding: 4px 8px; font-size: .78rem; }}
    video {{ display: block; width: 100%; height: auto; margin: 10px 0 16px; background: #000; }}
    audio {{ display: block; width: 100%; margin: 10px 0 16px; }}
    .setmap {{ margin: 8px 0 18px; padding-left: 1.1rem; }}
    .setmap li {{ margin: 4px 0; }}
    .transport {{
      position: static;
      display: flex; gap: 10px; flex-wrap: wrap; align-items: center;
      width: min(1180px, calc(100% - 2rem)); margin: 8px auto 28px;
      padding: 10px 0; background: transparent; border-top: 1px solid var(--line);
    }}
    @media (max-width: 860px) {{
      .stage {{ grid-template-columns: 1fr; }}
      .top nav {{ display: none; }}
    }}
  </style>
</head>
<body>
  <header class="top">
    <a class="brand" href="index.html">Chillhop Melodies</a>
    <nav>
      <a href="#roll">Roll</a>
      <a href="#files">Files</a>
      <a href="#reading">Recorded reading</a>
      <a href="media.html">Stills</a>
      <a href="midi/arrangement.mid">Arrangement</a>
    </nav>
  </header>
  <main>
    <section class="stage">
      <div>
        <p class="kicker">Eight 8-bar motifs · pocket, answer, space</p>
        <h1 id="title">Second Sixteenth</h1>
        <p id="identity"></p>
        <p class="meta" id="facts"></p>
        <p id="rhythm"></p>
        <p id="voicing"></p>
        <p id="layering"></p>
        <p id="accent-copy"></p>
        <p class="note" id="limits"></p>
        <p class="note" id="departures"></p>
      </div>
      <div id="roll">
        <figure class="hero">
          <img src="art/hero.jpg" width="1280" height="720" alt="Illustration of a short dusk melody, with gaps between the bars. Not a photograph of a studio or of performers.">
        </figure>
        <div class="rail" id="rail"></div>
        <div class="switch">
          <button type="button" id="var-a" aria-pressed="true">Variation A</button>
          <button type="button" id="var-b" aria-pressed="false">Variation B</button>
        </div>
        <div class="phrases" id="phrases"></div>
        <div class="scroller" id="scroller">
          <div class="ruler" id="ruler"></div>
          <div class="lane" id="melody"><div class="lane-label">Melody, from the melody file</div></div>
          <div class="keys-lane" id="keyslane"><div class="lane-label">Keys reference, not in the melody file</div></div>
          <div class="bass-lane" id="basslane"><div class="lane-label">Bass reference, not in the melody file</div></div>
        </div>
        <div class="spark" id="spark" aria-hidden="true"></div>
        <p class="legend">
          <span><i class="swatch" style="background:#2c1a12"></i>melody</span>
          <span><i class="swatch" style="background:#8c4e3a"></i>velocity 96 and up</span>
          <span><i class="swatch" style="background:#e28a3c"></i>keys reference</span>
          <span><i class="swatch" style="background:#f0c27a"></i>bass reference</span>
          <span>Bar height follows velocity. Gaps are rests.</span>
        </p>
        <p class="note" id="status">Reading the MIDI.</p>
      </div>
    </section>
    <p>{catalog['range_statement']}</p>
    <p class="note">{catalog['container_choice']} {catalog['note_policy']}</p>
    <h2>File contract</h2>
    <div class="flow">
      <span>Canonical score</span><span>MIDI</span><span>Reopened validation</span><span>MP3</span><span>Film</span>
    </div>
    <div class="flow">
      <span>Stills</span><span>Social drafts</span>
    </div>
    <div class="flow">
      <span>Catalog</span><span>This page</span>
    </div>
    <h2>Set map</h2>
    <ul class="setmap">{''.join(set_map)}</ul>
    <p class="note"><a href="articles/medium-draft-Cursor.md">Article draft</a> · <a href="articles/medium-paste-Cursor.txt">plain text</a></p>
    <p>{WARNING}</p>
    <h2 id="files">Files</h2>
    <p class="meta">Validation {report['result']}. Core {catalog['core_part_count']}. References {catalog['reference_part_count']}. <a href="midi/validation-Cursor.json">validation report</a> · <a href="catalog/catalog-Cursor.json">catalog</a> · <a href="score/canonical-score-Cursor.json">canonical score</a></p>
    <div class="table-scroll">
      <table>
        <thead><tr><th>Part</th><th>Role</th><th>Var</th><th>Count</th><th>BPM</th><th>Notes</th></tr></thead>
        <tbody>{''.join(rows)}</tbody>
      </table>
    </div>
    <section id="reading">
      <p class="kicker">Recorded reading · study 01 variation A, all 8 bars</p>
      <p>This MP3 is {seconds} seconds. {PREVIEW_LINE}. The film is {film_seconds} seconds and shows {ON_PICTURE}.</p>
      <audio controls preload="metadata" src="preview/preview.mp3"></audio>
      <p><a href="preview/preview.mp3">preview/preview.mp3</a> · <a href="preview/preview-manifest-Cursor.txt">preview manifest</a></p>
      <video controls preload="metadata" poster="film/poster.jpg" width="1280" height="720">
        <source src="film/preview.mp4" type="video/mp4">
        <track kind="captions" src="film/preview.vtt" srclang="en" label="English" default>
      </video>
    </section>
    <p>{PROGRAM}</p>
    <p>{AUDITION}</p>
    <p>{PUBLICATION}</p>
  </main>
  <div class="transport">
    <button type="button" id="play">Play melody</button>
    <button type="button" id="keys-toggle" aria-pressed="false">Keys reference</button>
    <button type="button" id="bass-toggle" aria-pressed="false">Bass reference</button>
    <span id="transport-label">Space plays. J and K change study.</span>
  </div>
  <script id="pack" type="application/json">{data}</script>
  <script>
    const pack = JSON.parse(document.getElementById("pack").textContent);
    const rail = document.getElementById("rail");
    const phrases = document.getElementById("phrases");
    const scroller = document.getElementById("scroller");
    const ruler = document.getElementById("ruler");
    const melody = document.getElementById("melody");
    const keyslane = document.getElementById("keyslane");
    const basslane = document.getElementById("basslane");
    const spark = document.getElementById("spark");
    const status = document.getElementById("status");
    let studyId = "s01";
    let variation = "a";
    let melodyNotes = [];
    let keysNotes = [];
    let bassNotes = [];
    let showKeys = false;
    let showBass = false;
    let audio = null;
    let playing = false;
    let followId = 0;
    let rollWidth = 1200;

    function study() {{
      return pack.studies.find((item) => item.id === studyId);
    }}
    function pitchName(pitch) {{
      return study().spell[pitch % 12] + (Math.floor(pitch / 12) - 1);
    }}
    function readVlq(view, offset) {{
      let value = 0;
      let byte = 0;
      do {{
        byte = view.getUint8(offset);
        offset += 1;
        value = (value << 7) | (byte & 0x7f);
      }} while (byte & 0x80);
      return [value, offset];
    }}
    function parseMidi(buffer) {{
      const view = new DataView(buffer);
      if (String.fromCharCode(view.getUint8(0), view.getUint8(1), view.getUint8(2), view.getUint8(3)) !== "MThd" || view.getUint16(12) !== 960) {{
        throw new Error("unexpected MIDI header");
      }}
      const tracks = view.getUint16(10);
      let offset = 14;
      const notes = [];
      for (let track = 0; track < tracks; track += 1) {{
        if (String.fromCharCode(view.getUint8(offset), view.getUint8(offset + 1), view.getUint8(offset + 2), view.getUint8(offset + 3)) !== "MTrk") {{
          throw new Error("missing track");
        }}
        const length = view.getUint32(offset + 4);
        offset += 8;
        const end = offset + length;
        let tick = 0;
        let running = 0;
        const open = new Map();
        while (offset < end) {{
          let delta;
          [delta, offset] = readVlq(view, offset);
          tick += delta;
          let byte = view.getUint8(offset);
          if (byte >= 0x80) {{
            running = byte;
            offset += 1;
          }}
          if (running === 0xff) {{
            offset += 1;
            let metaLen;
            [metaLen, offset] = readVlq(view, offset);
            offset += metaLen;
            continue;
          }}
          const kind = running & 0xf0;
          const data1 = byte < 0x80 ? byte : view.getUint8(offset);
          if (byte >= 0x80) offset += 1;
          let data2 = 0;
          if (kind !== 0xc0 && kind !== 0xd0) {{
            data2 = view.getUint8(offset);
            offset += 1;
          }}
          const key = (running & 0x0f) + ":" + data1;
          if (kind === 0x90 && data2 > 0) open.set(key, {{ tick: tick, velocity: data2 }});
          else if (kind === 0x80 || (kind === 0x90 && data2 === 0)) {{
            const started = open.get(key);
            if (started) {{
              notes.push({{ pitch: data1, start: started.tick, duration: tick - started.tick, velocity: started.velocity }});
              open.delete(key);
            }}
          }}
        }}
      }}
      notes.sort((a, b) => a.start - b.start || a.pitch - b.pitch);
      return notes;
    }}
    function partPath(role) {{
      const found = pack.parts.find((part) => part.study_id === studyId && part.role === role && part.variation === variation);
      if (!found) throw new Error("missing " + role);
      return found.path;
    }}
    function renderCopy() {{
      const item = study();
      document.getElementById("title").textContent = item.title;
      document.getElementById("identity").textContent = item.identity;
      document.getElementById("facts").textContent = item.id + " · " + item.bpm + " BPM · " + item.bars + " bars · " + item.seconds.toFixed(2) + " s · " + item.collection + " · tonic " + item.tonic;
      document.getElementById("rhythm").textContent = item.harmonic_rhythm;
      document.getElementById("voicing").textContent = item.voicing;
      document.getElementById("layering").textContent = item.layering;
      document.getElementById("accent-copy").textContent = item.accent;
      document.getElementById("limits").textContent = item.limitations;
      document.getElementById("departures").textContent = item.departures.length ? item.departures.join(" ") : "No pitch in this study is flagged as a departure.";
      document.getElementById("transport-label").textContent = item.title + " " + variation.toUpperCase() + " · Space plays · J and K change study";
      for (const button of rail.querySelectorAll("button")) button.setAttribute("aria-pressed", button.dataset.id === studyId ? "true" : "false");
      document.getElementById("var-a").setAttribute("aria-pressed", variation === "a" ? "true" : "false");
      document.getElementById("var-b").setAttribute("aria-pressed", variation === "b" ? "true" : "false");
      phrases.innerHTML = "";
      item.phrases.forEach((phrase) => {{
        const button = document.createElement("button");
        button.type = "button";
        button.textContent = phrase.name;
        button.addEventListener("click", () => {{
          const x = (phrase.start_bar / item.bars) * rollWidth;
          scroller.scrollTo({{ left: Math.max(0, x - 12), behavior: "smooth" }});
        }});
        phrases.appendChild(button);
      }});
    }}
    function melodyLane(notes) {{
      melody.querySelectorAll(".block, .phrase-band, .empty").forEach((node) => node.remove());
      const item = study();
      const container = item.bars * 4 * 960;
      if (!notes.length) {{
        const empty = document.createElement("p");
        empty.className = "empty lane-label";
        empty.textContent = "No melody notes.";
        melody.appendChild(empty);
        return;
      }}
      const low = Math.min(...notes.map((note) => note.pitch));
      const high = Math.max(...notes.map((note) => note.pitch));
      const span = Math.max(1, high - low);
      item.phrases.forEach((phrase, index) => {{
        if (index % 2) return;
        const band = document.createElement("div");
        band.className = "phrase-band";
        band.style.left = (phrase.start_bar / item.bars) * rollWidth + "px";
        band.style.width = (phrase.bars / item.bars) * rollWidth + "px";
        melody.appendChild(band);
      }});
      notes.forEach((note) => {{
        const block = document.createElement("div");
        block.className = "block" + (note.velocity >= 96 ? " hot" : "");
        block.title = pitchName(note.pitch) + " · velocity " + note.velocity;
        const y = 28 + (1 - (note.pitch - low) / span) * 100;
        block.style.left = (note.start / container) * rollWidth + "px";
        block.style.width = Math.max(3, (note.duration / container) * rollWidth - 1) + "px";
        block.style.top = y + "px";
        block.style.height = (8 + (note.velocity / 127) * 18) + "px";
        melody.appendChild(block);
      }});
    }}
    function referenceLane(host, notes, klass) {{
      host.querySelectorAll(".knote, .bnote").forEach((node) => node.remove());
      if (!host.classList.contains("on")) return;
      const item = study();
      const container = item.bars * 4 * 960;
      notes.forEach((note) => {{
        const mark = document.createElement("div");
        mark.className = klass;
        mark.title = pitchName(note.pitch);
        mark.style.left = (note.start / container) * rollWidth + "px";
        mark.style.width = Math.max(3, (note.duration / container) * rollWidth - 1) + "px";
        host.appendChild(mark);
      }});
    }}
    function draw() {{
      const item = study();
      rollWidth = Math.max(960, item.bars * 210);
      [ruler, melody, keyslane, basslane].forEach((node) => {{ node.style.width = rollWidth + "px"; }});
      ruler.innerHTML = "";
      let bar = 0;
      item.changes.forEach((name, index) => {{
        const span = item.change_bars[index];
        const mark = document.createElement("div");
        mark.className = "change";
        mark.textContent = name;
        mark.style.left = (bar / item.bars) * rollWidth + "px";
        mark.style.width = (span / item.bars) * rollWidth + "px";
        ruler.appendChild(mark);
        bar += span;
      }});
      melodyLane(melodyNotes);
      keyslane.classList.toggle("on", showKeys);
      basslane.classList.toggle("on", showBass);
      referenceLane(keyslane, keysNotes, "knote");
      referenceLane(basslane, bassNotes, "bnote");
      spark.innerHTML = "";
      melodyNotes.forEach((note) => {{
        const bar = document.createElement("i");
        bar.style.height = Math.max(4, (note.velocity / 127) * 46) + "px";
        spark.appendChild(bar);
      }});
      status.textContent = melodyNotes.length + " melody notes from the melody file. Keys and bass stay in their own lanes.";
    }}
    async function loadStudy() {{
      stopPlayback();
      renderCopy();
      status.textContent = "Reading the MIDI.";
      try {{
        const melodyRes = await fetch(partPath("melody"));
        const keysRes = await fetch(partPath("keys-reference"));
        const bassRes = await fetch(partPath("bass-reference"));
        if (!melodyRes.ok || !keysRes.ok || !bassRes.ok) throw new Error("MIDI request failed");
        melodyNotes = parseMidi(await melodyRes.arrayBuffer());
        keysNotes = parseMidi(await keysRes.arrayBuffer());
        bassNotes = parseMidi(await bassRes.arrayBuffer());
        draw();
      }} catch (error) {{
        melodyNotes = [];
        keysNotes = [];
        bassNotes = [];
        status.textContent = "The MIDI did not load. " + error.message;
      }}
    }}
    function freq(pitch) {{
      return 440 * Math.pow(2, (pitch - 69) / 12);
    }}
    function schedule(ctx, note, origin, amount, type) {{
      const item = study();
      const seconds = (tick) => tick / 960 * item.tempo_us / 1000000;
      const when = origin + seconds(note.start);
      const duration = Math.max(0.04, seconds(note.duration));
      const osc = ctx.createOscillator();
      const gain = ctx.createGain();
      osc.type = type;
      osc.frequency.value = freq(note.pitch);
      const level = amount * (note.velocity / 110);
      const attack = Math.min(0.02, duration * 0.2);
      gain.gain.setValueAtTime(0.0001, when);
      gain.gain.exponentialRampToValueAtTime(Math.max(0.0002, level), when + attack);
      gain.gain.exponentialRampToValueAtTime(0.0001, when + duration);
      osc.connect(gain);
      gain.connect(ctx.destination);
      osc.start(when);
      osc.stop(when + duration + 0.02);
    }}
    function stopPlayback() {{
      playing = false;
      cancelAnimationFrame(followId);
      if (audio) audio.close();
      audio = null;
      document.getElementById("play").textContent = "Play melody";
    }}
    function playMelody() {{
      if (!melodyNotes.length) return;
      stopPlayback();
      const ctx = new AudioContext();
      audio = ctx;
      playing = true;
      document.getElementById("play").textContent = "Stop";
      const origin = ctx.currentTime + 0.05;
      melodyNotes.forEach((note) => {{
        schedule(ctx, note, origin, 0.07, "triangle");
        schedule(ctx, note, origin, 0.03, "sine");
      }});
      if (showKeys) keysNotes.forEach((note) => schedule(ctx, note, origin, 0.02, "triangle"));
      if (showBass) bassNotes.forEach((note) => schedule(ctx, note, origin, 0.06, "sine"));
      const item = study();
      const container = item.bars * 4 * 60 / item.bpm;
      const follow = () => {{
        if (!playing || !audio) return;
        if (audio.currentTime - origin < container) followId = requestAnimationFrame(follow);
        else stopPlayback();
      }};
      follow();
    }}
    function stepStudy(direction) {{
      const index = pack.studies.findIndex((item) => item.id === studyId);
      studyId = pack.studies[(index + direction + pack.studies.length) % pack.studies.length].id;
      loadStudy();
    }}
    pack.studies.forEach((item) => {{
      const button = document.createElement("button");
      button.type = "button";
      button.dataset.id = item.id;
      button.textContent = item.id.slice(1) + " " + item.title;
      button.addEventListener("click", () => {{ studyId = item.id; loadStudy(); }});
      rail.appendChild(button);
    }});
    document.getElementById("var-a").addEventListener("click", () => {{ variation = "a"; loadStudy(); }});
    document.getElementById("var-b").addEventListener("click", () => {{ variation = "b"; loadStudy(); }});
    document.getElementById("play").addEventListener("click", () => {{ if (playing) stopPlayback(); else playMelody(); }});
    document.getElementById("keys-toggle").addEventListener("click", () => {{
      showKeys = !showKeys;
      document.getElementById("keys-toggle").setAttribute("aria-pressed", showKeys ? "true" : "false");
      if (melodyNotes.length) draw();
    }});
    document.getElementById("bass-toggle").addEventListener("click", () => {{
      showBass = !showBass;
      document.getElementById("bass-toggle").setAttribute("aria-pressed", showBass ? "true" : "false");
      if (melodyNotes.length) draw();
    }});
    window.addEventListener("keydown", (event) => {{
      const tag = document.activeElement && document.activeElement.tagName;
      if (tag === "INPUT" || tag === "TEXTAREA" || tag === "AUDIO" || tag === "VIDEO") return;
      if (event.code === "Space") {{ event.preventDefault(); if (playing) stopPlayback(); else playMelody(); }}
      else if (event.key === "j" || event.key === "J") stepStudy(-1);
      else if (event.key === "k" || event.key === "K") stepStudy(1);
    }});
    loadStudy();
  </script>
</body>
</html>
"""
