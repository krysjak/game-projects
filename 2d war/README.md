# Historical Video Generator - Offline Agent

An educational video generation system that creates historical content with synthetic speech, cinematic effects, and comprehensive safety filters.

## Features

- **Multi-language Support**: English, Spanish, Ukrainian
- **Multiple Voice Profiles**: Deep male retro, neutral female, authoritative male, documentary female
- **Style Templates**: Authoritarian, documentary, neutral narrator, lecture
- **Video Effects**: Vintage, cinematic, sepia tone, grain, vignette, Ken Burns zoom
- **Safety Filters**: Blocks violence incitement, hate speech, illegal activity promotion
- **Complete Output Package**: Text, audio, video, subtitles, metadata

## Ethical Safeguards

✅ **NO voice cloning** - Uses only synthetic neural voices  
✅ **NO face cloning** - Processes still images only  
✅ **Clear disclaimers** - All outputs labeled as synthetic content  
✅ **Safety filtering** - Blocks harmful content automatically  
✅ **Full transparency** - Metadata logs all settings and models used  

## Installation

### Requirements

- Python 3.8+
- FFmpeg (for video processing)

### Install FFmpeg

**Windows:**
```bash
# Download from https://ffmpeg.org/download.html
# Add to PATH
```

**Linux:**
```bash
sudo apt-get install ffmpeg
```

**macOS:**
```bash
brew install ffmpeg
```

### Install Python Dependencies

```bash
pip install -r requirements.txt
```

## Usage

### Basic Command

```bash
python main.py \
  --photo_path "path/to/photo.jpg" \
  --topic "A historical moment from World War II showing soldiers" \
  --language en \
  --voice_profile deep_male_retro \
  --style_template documentary \
  --duration_seconds 10
```

### Parameters

| Parameter | Required | Options | Default | Description |
|-----------|----------|---------|---------|-------------|
| `--photo_path` | Yes | File path | - | Input photo/image |
| `--topic` | Yes | Text | - | Speech topic (1-2 sentences) |
| `--language` | No | en/es/uk | en | Language code |
| `--voice_profile` | No | See below | neutral_female | Voice to use |
| `--style_template` | No | See below | documentary | Speech style |
| `--duration_seconds` | No | 2-20 | 10 | Video duration |
| `--output_dir` | No | Directory | output | Output folder |

### Voice Profiles

- `deep_male_retro` - Deep male voice with reverb (1940s newsreel style)
- `neutral_female` - Clear female voice
- `authoritative_male` - British-accented authoritative male
- `documentary_female` - Warm documentary narrator

### Style Templates

- `authoritarian` - Short, emphatic sentences with commanding tone
- `documentary` - Engaging, informative narrative
- `neutral_narrator` - Objective, educational tone
- `lecture` - Academic, thoughtful presentation

## Output Files

For each generation, the system creates:

```
output/
  video_20241015_143022_text.txt        # Speech transcript
  video_20241015_143022_speech.wav      # Audio file
  video_20241015_143022_video.mp4       # Final video
  video_20241015_143022_subtitles.srt   # Subtitle file
  video_20241015_143022_metadata.json   # Generation metadata
```

## Examples

### Example 1: Documentary Style

```bash
python main.py \
  --photo_path "examples/photo1.jpg" \
  --topic "The liberation of Paris in 1944" \
  --style_template documentary \
  --voice_profile documentary_female \
  --duration_seconds 15
```

### Example 2: Authoritarian Newsreel

```bash
python main.py \
  --photo_path "examples/photo2.jpg" \
  --topic "Industrial workers contribute to the war effort" \
  --style_template authoritarian \
  --voice_profile deep_male_retro \
  --duration_seconds 8 \
  --language en
```

### Example 3: Academic Lecture

```bash
python main.py \
  --photo_path "examples/photo3.jpg" \
  --topic "Examining the social changes during the Cold War era" \
  --style_template lecture \
  --voice_profile authoritative_male \
  --duration_seconds 20
```

### Example 4: Spanish Documentary

```bash
python main.py \
  --photo_path "examples/photo4.jpg" \
  --topic "La Guerra Civil Española y su impacto" \
  --language es \
  --style_template documentary \
  --voice_profile documentary_female \
  --duration_seconds 12
```

## Configuration

Edit `config.yaml` to customize:

- Voice parameters (pitch, speed, reverb)
- Video effects and quality settings
- Safety filter patterns
- Output format specifications

## Safety Features

The system includes multiple safety layers:

1. **Content Filtering**: Blocks requests containing:
   - Violence incitement
   - Hate speech
   - Illegal activity instructions
   - Extreme political violence

2. **Automatic Rewriting**: Softens extreme language while maintaining educational value

3. **Mandatory Disclaimers**: All outputs include clear synthetic content labels

4. **Metadata Logging**: Full transparency about generation process

## Technical Architecture

```
main.py
  └─> HistoricalVideoGenerator
       ├─> SpeechGenerator (template-based text generation)
       ├─> TTSEngine (edge-tts for synthetic voices)
       ├─> VideoComposer (moviepy + effects)
       ├─> SubtitleGenerator (SRT creation)
       └─> SafetyFilter (content moderation)
```

## Limitations

- Duration: 2-20 seconds per video
- Input: Static images only (no video input)
- Voices: Synthetic only (no real person cloning)
- Languages: Currently supports English, Spanish, Ukrainian
- Requires internet for first-time voice model download

## Troubleshooting

### "FFmpeg not found"
Ensure FFmpeg is installed and in your system PATH.

### "Voice not available"
Run `edge-tts --list-voices` to see available voices for your language.

### "Content blocked"
Your topic contains prohibited content. Revise to focus on educational/historical facts.

### "Audio/video sync issues"
Adjust `duration_seconds` to better match the speech length.

## License

This software is provided for educational purposes only. Users are responsible for ensuring their use complies with all applicable laws and ethical standards.

## Disclaimer

All voices and content generated by this system are **synthetic and artificial**. This system does NOT clone real persons' voices or faces. Any resemblance is coincidental. Always clearly label generated content as synthetic.

