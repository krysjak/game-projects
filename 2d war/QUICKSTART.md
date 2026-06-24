# Quick Start Guide

## Step 1: Install Dependencies

### Install FFmpeg

**Windows:**
1. Download from https://ffmpeg.org/download.html
2. Extract to `C:\ffmpeg`
3. Add `C:\ffmpeg\bin` to System PATH

**Linux:**
```bash
sudo apt-get update
sudo apt-get install ffmpeg
```

**macOS:**
```bash
brew install ffmpeg
```

### Install Python Packages

```bash
pip install -r requirements.txt
```

## Step 2: Verify Setup

```bash
python setup.py
```

This will check:
- Python version (3.8+ required)
- FFmpeg installation
- Python dependencies
- Configuration files

## Step 3: Generate Your First Video

### Option A: Use Example Script

```bash
python example_usage.py 1
```

This creates a sample photo and generates a documentary-style video.

### Option B: Use Your Own Photo

```bash
python main.py \
  --photo_path "path/to/your/photo.jpg" \
  --topic "Describe the historical moment in 1-2 sentences" \
  --style_template documentary \
  --voice_profile documentary_female \
  --duration_seconds 10
```

## Step 4: Check Output

Look in the `output/` directory for:
- `*_video.mp4` - Your generated video
- `*_speech.wav` - The audio narration
- `*_text.txt` - The speech transcript
- `*_subtitles.srt` - Subtitle file
- `*_metadata.json` - Generation details

## Available Styles

| Style | Description | Best For |
|-------|-------------|----------|
| `documentary` | Engaging narrative | Educational content |
| `authoritarian` | Commanding, emphatic | Historical propaganda style |
| `neutral_narrator` | Objective, clear | General information |
| `lecture` | Academic, analytical | Deep dives, analysis |

## Available Voices

| Voice Profile | Description |
|---------------|-------------|
| `documentary_female` | Warm, engaging female voice |
| `deep_male_retro` | Deep male with reverb (1940s style) |
| `authoritative_male` | British-accented male |
| `neutral_female` | Clear, neutral female |

## Language Support

- `en` - English
- `es` - Spanish (Español)
- `uk` - Ukrainian (Українська)

## Example Commands

### English Documentary
```bash
python main.py \
  --photo_path "photo.jpg" \
  --topic "The fall of the Berlin Wall symbolized the end of the Cold War era" \
  --language en \
  --style_template documentary \
  --voice_profile documentary_female \
  --duration_seconds 12
```

### Spanish Authoritarian Style
```bash
python main.py \
  --photo_path "photo.jpg" \
  --topic "La revolución industrial transformó la sociedad europea" \
  --language es \
  --style_template authoritarian \
  --voice_profile deep_male_retro \
  --duration_seconds 10
```

### Ukrainian Academic Lecture
```bash
python main.py \
  --photo_path "photo.jpg" \
  --topic "Аналіз соціальних змін у післявоєнний період" \
  --language uk \
  --style_template lecture \
  --voice_profile authoritative_male \
  --duration_seconds 15
```

## Troubleshooting

### "FFmpeg not found"
- Verify FFmpeg is installed: `ffmpeg -version`
- On Windows, ensure FFmpeg is in your PATH
- Restart terminal after installation

### "Module not found"
```bash
pip install -r requirements.txt --upgrade
```

### "Content blocked by safety filter"
Your topic contains prohibited content. Focus on:
- Historical facts and analysis
- Educational information
- Objective descriptions
Avoid:
- Calls to violence
- Hate speech
- Illegal activity instructions

### Video/audio not syncing
Adjust `--duration_seconds` to match speech length. Longer topics need more time.

## Tips

1. **Photo Quality**: Use high-resolution images (1920x1080 or higher)
2. **Topic Length**: Keep topics concise (1-2 sentences) for best results
3. **Duration**: Match duration to topic complexity
   - Simple facts: 5-8 seconds
   - Descriptions: 10-15 seconds
   - Analysis: 15-20 seconds
4. **Voice Selection**: Match voice to content
   - Documentary: Use documentary_female
   - Historical footage: Use deep_male_retro
   - Academic: Use authoritative_male

## Ethics Reminder

This tool generates **synthetic content only**:
- ✅ Uses synthetic neural voices (not real person clones)
- ✅ Processes static images (no face manipulation)
- ✅ Adds clear disclaimers to all outputs
- ✅ Filters harmful content automatically

Always label generated content as synthetic and educational.

## Next Steps

- Experiment with different styles and voices
- Adjust `config.yaml` for custom voice parameters
- Create a collection of historical videos
- Share responsibly with proper attribution

## Support

For issues or questions, check:
1. `README.md` - Full documentation
2. `setup.py` - Run setup verification
3. `example_usage.py` - See working examples

