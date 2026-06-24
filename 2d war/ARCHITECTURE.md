# System Architecture

## Overview

The Historical Video Generator is a modular Python application that transforms a static photo and topic description into an educational video with synthetic narration, effects, and subtitles.

## Architecture Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                         main.py                              │
│                    (CLI Interface)                           │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────┐
│                  video_generator.py                          │
│              (Orchestration Layer)                           │
└─────┬──────┬──────┬──────┬──────┬──────────────────────────┘
      │      │      │      │      │
      ▼      ▼      ▼      ▼      ▼
   ┌───┐  ┌───┐  ┌───┐  ┌───┐  ┌───┐
   │ 1 │  │ 2 │  │ 3 │  │ 4 │  │ 5 │
   └─┬─┘  └─┬─┘  └─┬─┘  └─┬─┘  └─┬─┘
     │      │      │      │      │
     ▼      ▼      ▼      ▼      ▼
┌────────────────────────────────────────────────────────────┐
│  1. SafetyFilter    - Content moderation                   │
│  2. SpeechGenerator - Text creation with style templates   │
│  3. TTSEngine       - Text-to-speech synthesis             │
│  4. VideoComposer   - Video effects and composition        │
│  5. SubtitleGenerator - SRT subtitle creation              │
└────────────────────────────────────────────────────────────┘
```

## Module Descriptions

### 1. main.py
**Purpose**: Command-line interface and entry point

**Responsibilities**:
- Parse command-line arguments
- Validate inputs
- Instantiate `HistoricalVideoGenerator`
- Display results to user

**Key Functions**:
- `main()` - CLI entry point
- Argument parsing with `argparse`
- Input validation

### 2. video_generator.py
**Purpose**: Orchestration layer coordinating all modules

**Class**: `HistoricalVideoGenerator`

**Responsibilities**:
- Coordinate the 6-step generation pipeline
- Manage file I/O
- Create metadata
- Handle errors gracefully

**Pipeline Steps**:
1. Safety filter check
2. Generate speech text
3. Synthesize audio (TTS)
4. Generate subtitles
5. Compose video with effects
6. Create metadata file

**Key Methods**:
- `generate()` - Main orchestration method
- Returns dict with paths to all generated files

### 3. speech_generator.py
**Purpose**: Generate speech text based on templates

**Class**: `SpeechGenerator`

**Responsibilities**:
- Apply style templates (authoritarian, documentary, etc.)
- Adapt to language
- Insert prosody markers for TTS
- Match content to target duration

**Style Templates**:
- **Authoritarian**: Short, emphatic, commanding
- **Documentary**: Engaging, narrative, informative
- **Neutral Narrator**: Objective, educational
- **Lecture**: Academic, analytical, thoughtful

**Key Methods**:
- `generate()` - Main text generation
- `_generate_authoritarian()` - Authoritarian style
- `_generate_documentary()` - Documentary style
- `_generate_lecture()` - Lecture style
- `_generate_neutral()` - Neutral narrator style
- `_add_prosody_hints()` - Add pause markers

**Output Format**:
```
Text with [PAUSE=0.3s] markers for prosody
```

### 4. tts_engine.py
**Purpose**: Text-to-speech synthesis

**Class**: `TTSEngine`

**Responsibilities**:
- Convert text to speech audio
- Apply voice profiles (pitch, speed, reverb)
- Handle multiple languages
- Use neural voices (not voice cloning)

**Technology**: 
- Uses `edge-tts` (Microsoft Edge Neural Voices)
- Supports SSML for prosody control

**Voice Profiles**:
```yaml
deep_male_retro:
  pitch: -20Hz
  speed: 0.9x
  reverb: 0.3

neutral_female:
  pitch: 0Hz
  speed: 1.0x
  reverb: 0.1
```

**Language Mapping**:
- English → en-US-*, en-GB-*
- Spanish → es-ES-*, es-MX-*
- Ukrainian → uk-UA-*

**Key Methods**:
- `generate()` - Synthesize audio
- `_convert_to_ssml()` - Convert pause markers to SSML
- `_get_voice_for_language()` - Map voices to languages

**Output**: WAV audio file

### 5. video_composer.py
**Purpose**: Video creation with cinematic effects

**Class**: `VideoComposer`

**Responsibilities**:
- Load and preprocess images
- Apply visual effects (vintage, cinematic, etc.)
- Synchronize with audio
- Add disclaimer overlay
- Render final video

**Effects Pipeline**:
```
Input Photo
    ↓
Resize & Crop to 1920x1080
    ↓
Apply Style Effects:
  - Sepia tone
  - Film grain
  - Vignette
  - Slight blur
    ↓
Apply Motion Effects:
  - Ken Burns zoom/pan
  - Fade in/out
    ↓
Add Disclaimer Overlay
    ↓
Composite with Audio
    ↓
Render to MP4
```

**Technology**:
- `moviepy` for video composition
- `PIL` (Pillow) for image processing
- `numpy` for array operations

**Key Methods**:
- `compose()` - Main composition
- `_preprocess_image()` - Image preparation
- `_apply_vintage_effect()` - Retro styling
- `_sepia_tone()` - Sepia color grading
- `_add_grain()` - Film grain effect
- `_add_vignette()` - Edge darkening
- `_apply_effects()` - Motion effects
- `_create_disclaimer_overlay()` - Text overlay

**Output Settings**:
```yaml
codec: libx264
audio_codec: aac
fps: 24
resolution: [1920, 1080]
bitrate: 5000k
```

### 6. subtitle_generator.py
**Purpose**: Create SRT subtitle files

**Class**: `SubtitleGenerator`

**Responsibilities**:
- Parse speech text
- Time subtitles to audio duration
- Generate SRT format

**Process**:
1. Clean prosody markers from text
2. Split text into sentences
3. Calculate time per sentence
4. Create SRT entries with timestamps
5. Write .srt file

**Key Methods**:
- `generate()` - Create SRT file
- `_clean_prosody_markers()` - Remove [PAUSE=X] tags
- `_split_into_sentences()` - Sentence segmentation

**Output Format** (SRT):
```
1
00:00:00,000 --> 00:00:03,500
First sentence of narration.

2
00:00:03,500 --> 00:00:07,000
Second sentence of narration.
```

### 7. safety_filter.py
**Purpose**: Content moderation and safety

**Class**: `SafetyFilter`

**Responsibilities**:
- Block harmful content
- Filter extreme language
- Rewrite acceptable content softly

**Blocked Content**:
- Violence incitement
- Hate speech
- Illegal activity instructions
- Extreme political violence

**Filter Patterns** (regex):
```python
- \b(kill|murder|attack)\s+(all|the)\s+
- \b(genocide|massacre)\b
- \bcall\s+to\s+violence\b
- \bfinal\s+solution\b
- \b(how\s+to)\s+make\s+bomb\b
```

**Key Methods**:
- `check_and_filter()` - Main filtering
- `_compile_patterns()` - Prepare regex patterns

**Return**:
- `(is_safe: bool, filtered_text: str)`

## Configuration (config.yaml)

### Structure
```yaml
voice_profiles:
  [voice_name]:
    gender: male/female
    pitch: -20 to +20 Hz
    speed: 0.8 to 1.2x
    reverb: 0.0 to 0.5
    voice_id: "edge-tts voice ID"

style_templates:
  [style_name]:
    tone: "description"
    pause_pattern: "frequency"
    sentence_structure: "style"
    rhetoric: "devices used"

video_effects:
  [effect_set]:
    - effect_1
    - effect_2

output:
  video_codec: "libx264"
  audio_codec: "aac"
  fps: 24
  resolution: [1920, 1080]
```

## Data Flow

```
User Input
  ↓
photo_path, topic, language, voice_profile, style_template, duration
  ↓
┌──────────────────────────┐
│ 1. Safety Filter         │ → Block if unsafe
└────────┬─────────────────┘
         ↓ (Safe topic)
┌──────────────────────────┐
│ 2. Speech Generator      │ → text.txt
└────────┬─────────────────┘
         ↓ (Speech text)
┌──────────────────────────┐
│ 3. TTS Engine           │ → speech.wav
└────────┬─────────────────┘
         ↓ (Audio file)
┌──────────────────────────┐
│ 4. Subtitle Generator    │ → subtitles.srt
└────────┬─────────────────┘
         ↓ (SRT file)
┌──────────────────────────┐
│ 5. Video Composer        │ → video.mp4
│   (photo + audio + srt)  │
└────────┬─────────────────┘
         ↓ (Video file)
┌──────────────────────────┐
│ 6. Metadata Generator    │ → metadata.json
└────────┬─────────────────┘
         ↓
Output Directory:
  - text.txt
  - speech.wav
  - subtitles.srt
  - video.mp4
  - metadata.json
```

## File Outputs

### text.txt
```
Synthetic content. Not an authentic speech by any real person.

[Generated speech text with prosody markers removed]
```

### speech.wav
- Format: WAV
- Sample rate: 24000 Hz (typical for edge-tts)
- Channels: Mono
- Duration: Matches speech length

### subtitles.srt
```
1
00:00:00,000 --> 00:00:05,000
First subtitle line

2
00:00:05,000 --> 00:00:10,000
Second subtitle line
```

### video.mp4
- Codec: H.264 (libx264)
- Resolution: 1920x1080
- FPS: 24
- Audio: AAC
- Contains: Photo with effects + audio + disclaimer overlay

### metadata.json
```json
{
  "timestamp": "20241015_143022",
  "datetime": "2025-10-15T14:30:22",
  "inputs": { ... },
  "outputs": { ... },
  "models": {
    "tts_engine": "edge-tts",
    "speech_generator": "rule-based template system v1.0"
  },
  "disclaimer": "Synthetic content. Not an authentic speech by any real person.",
  "ethics_note": "This content was generated using synthetic voices...",
  "safety_filter": "enabled"
}
```

## Dependencies

### Core Libraries
- **PIL (Pillow)** - Image processing
- **moviepy** - Video editing and composition
- **edge-tts** - Text-to-speech synthesis
- **pydub** - Audio processing
- **numpy** - Numerical operations
- **opencv-python** - Additional image/video processing
- **srt** - Subtitle file creation
- **pyyaml** - Configuration parsing

### External Requirements
- **FFmpeg** - Video encoding/decoding backend

## Error Handling

Each module includes error handling:
- Input validation
- File I/O error checking
- Graceful degradation
- Informative error messages

Example:
```python
try:
    result = generator.generate(...)
except ValueError as e:
    # Safety filter rejection
    print(f"Content blocked: {e}")
except FileNotFoundError as e:
    # Missing input file
    print(f"File not found: {e}")
except Exception as e:
    # General error
    print(f"Generation failed: {e}")
```

## Performance Considerations

- **Image preprocessing**: Cached after first load
- **TTS synthesis**: Async execution with edge-tts
- **Video rendering**: Uses moviepy with optimized settings
- **Typical generation time**: 10-30 seconds for 10-second video

## Security & Ethics

### Built-in Protections
1. **Content filtering** - Blocks harmful requests
2. **No cloning** - Only synthetic voices, no voice cloning
3. **Watermarking** - Disclaimer overlay on all videos
4. **Metadata logging** - Full transparency on generation
5. **Input sanitization** - Validates all inputs

### Compliance
- GDPR: No personal data collection
- Copyright: Users responsible for photo rights
- Synthetic Media: Clear labeling as required by law

## Extensibility

### Adding New Voice Profiles
Edit `config.yaml`:
```yaml
voice_profiles:
  my_custom_voice:
    gender: male
    pitch: -15
    speed: 1.05
    reverb: 0.25
    voice_id: "en-US-ChristopherNeural"
```

### Adding New Style Templates
Edit `config.yaml`:
```yaml
style_templates:
  my_custom_style:
    tone: "dramatic, emotional"
    pause_pattern: "frequent_long"
    sentence_structure: "varied"
    rhetoric: "imagery, metaphors"
```

Then add generation method in `speech_generator.py`:
```python
def _generate_my_custom_style(self, topic, target_words, language):
    # Implementation
    pass
```

### Adding New Video Effects
Edit `video_composer.py` to add new image processing or motion effects.

### Adding New Languages
1. Map language code in `tts_engine.py`
2. Add speech templates in `speech_generator.py`
3. Update edge-tts voice mappings

## Testing

Run the test suite:
```bash
python test_installation.py
```

This validates:
- All imports
- Module loading
- Configuration
- Safety filter functionality
- Speech generation

## Future Enhancements

Potential improvements:
- More languages (French, German, Chinese, etc.)
- Advanced prosody control (emotion, emphasis)
- Custom voice training (within ethical bounds)
- Video timeline editing
- Batch processing
- Web interface
- API endpoints

