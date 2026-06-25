# Game Projects

Two Python projects — an AI-powered historical video generator and an emergent art simulation game.

---

## 🎬 2D War — Historical Video Generator

Not a playable game — an **offline AI-agent pipeline** that generates short educational historical videos from a single still photo. The user provides a photo and a topic description; the system produces a complete narrated video package with synthetic speech, cinematic visual effects, and SRT subtitles.

### How it works
A linear 6-step pipeline orchestrated by `HistoricalVideoGenerator`:

```
Photo + Topic → SafetyFilter → SpeechGenerator → TTSEngine → VideoComposer → SubtitleGenerator
```

### Features
- **4 voice profiles** (synthetic, non-cloned): `deep_male_retro` (1940s newsreel), `neutral_female`, `authoritative_male` (British), `documentary_female`.
- **4 style templates**: `authoritarian`, `documentary`, `neutral_narrator`, `lecture` — each with distinct tone, pause pattern, sentence structure, and rhetoric.
- **3 video effect stacks**: `vintage` (sepia/grain/scanlines), `cinematic` (color-grade/zoom/fade), `documentary` (correction/zoom/fade-in-out).
- **3 languages**: English, Spanish, Ukrainian.
- **Safety filter** blocks violence incitement, hate speech, illegal activity. Softens extreme language automatically.
- **Output package** (timestamped): `_text.txt` (transcript), `_speech.wav` (audio), `_video.mp4` (H.264 1080p 24fps), `_subtitles.srt`, `_metadata.json`.
- Duration: 2–20 seconds per video. Static images only.

### Prerequisites
- Python 3.8+
- **FFmpeg** (must be on PATH)
- `pip install -r requirements.txt`

### Run
```bash
python main.py \
  --photo_path "path/to/photo.jpg" \
  --topic "A historical moment..." \
  --language en \
  --voice_profile neutral_female \
  --style_template documentary \
  --duration_seconds 10
```

### Verify setup
```bash
python setup.py   # checks Python, FFmpeg, and dependencies
```

---

## 🌌 Other World — Tree of Life Constellation Game

An emergent-behavior simulation built with **Pygame**. Not a traditional game — there is no win/lose condition. Colored points ("people") are spawned in "space" and attracted to 16 invisible tree-structure nodes. Through simple attraction physics, hundreds of points collectively self-organize into the visible shape of a tree.

### Mechanics
- **16 invisible attractor nodes** across 5 depth levels (root → trunk → branches → twigs → leaves). Deeper nodes attract more strongly.
- **Per-point physics**: primary tree-node attraction (`force ∝ strength / distance^1.5`), weak inter-point gravity (`G·m1·m2 / r²`), velocity damping (`*= 0.998`), 10-frame motion trails.
- Points spawn in waves with unique random colors from a 10-color palette.
- Lines connect nearby points to reveal the emergent tree structure.

### Controls
| Input | Action |
|-------|--------|
| Mouse wheel | Zoom |
| Right-click + drag | Pan camera |
| ESC | Quit |

### Run
```bash
pip install -r requirements.txt    # pygame==2.5.2
python constellation_game.py
```

---

## 📁 Project Structure

```
games/
├── 2d war/
│   ├── main.py                    # CLI entry (argparse)
│   ├── video_generator.py          # HistoricalVideoGenerator orchestrator
│   ├── speech_generator.py         # Text creation with style templates
│   ├── tts_engine.py               # edge-tts synthesis
│   ├── video_composer.py           # MoviePy visual effects
│   ├── subtitle_generator.py      # SRT creation
│   ├── safety_filter.py            # Content moderation
│   ├── config.yaml                 # Voice profiles, styles, effects
│   ├── setup.py                    # Setup verification
│   ├── requirements.txt
│   ├── README.md, ARCHITECTURE.md, QUICKSTART.md, LICENSE
│   └── (output/ and examples/ excluded from repo)
│
└── other world/
    ├── constellation_game.py        # Single-file Pygame simulation
    ├── requirements.txt
    └── README.md
```
