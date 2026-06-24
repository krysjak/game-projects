# Historical Video Generator - Project Summary

## What Is This?

An **offline, ethical video generation system** for creating educational historical content. It transforms a single photo and topic description into a professional narrated video with:

✅ Synthetic speech narration (multiple languages & voices)  
✅ Cinematic visual effects (vintage, sepia, Ken Burns)  
✅ Professional subtitles  
✅ Complete metadata tracking  
✅ Built-in safety filters  

## Key Features

### 🎙️ Text-to-Speech (TTS)
- **4 voice profiles**: Deep male retro, neutral female, authoritative male, documentary female
- **3 languages**: English, Spanish, Ukrainian
- **Neural synthesis**: Microsoft Edge Neural Voices (NOT cloned from real people)
- **Prosody control**: Adjustable pitch, speed, reverb, pauses

### 📝 Style Templates
- **Authoritarian**: 1940s newsreel style - commanding, emphatic, short sentences
- **Documentary**: Modern educational - engaging, narrative, informative
- **Neutral Narrator**: Objective journalism - clear, balanced, factual
- **Lecture**: Academic presentation - analytical, thoughtful, pedagogical

### 🎬 Video Effects
- **Vintage filter**: Sepia tone, film grain, vignette, blur
- **Motion**: Ken Burns zoom/pan effect
- **Transitions**: Fade in/out
- **Overlay**: Mandatory synthetic content disclaimer
- **Output**: 1920x1080 MP4, 24fps, H.264

### 🛡️ Safety & Ethics
- **Content filter**: Blocks violence, hate speech, illegal activities
- **No cloning**: Uses only synthetic voices, never clones real people
- **Transparency**: Full metadata logging with timestamps and models used
- **Disclaimers**: All outputs labeled as synthetic content
- **Responsible AI**: Designed for educational use only

## File Structure

```
2d war/
├── main.py                    # CLI entry point
├── video_generator.py         # Orchestration layer
├── speech_generator.py        # Text generation with templates
├── tts_engine.py             # Text-to-speech synthesis
├── video_composer.py         # Video effects and composition
├── subtitle_generator.py     # SRT subtitle creation
├── safety_filter.py          # Content moderation
├── config.yaml               # Configuration (voices, styles, effects)
├── requirements.txt          # Python dependencies
├── setup.py                  # Installation verification
├── test_installation.py      # Test suite
├── example_usage.py          # Example scripts
├── README.md                 # Main documentation
├── QUICKSTART.md             # Quick start guide
├── ARCHITECTURE.md           # Technical architecture
├── LICENSE                   # MIT License + Ethics notice
└── .gitignore               # Git ignore rules
```

## Quick Start

### 1. Install
```bash
# Install FFmpeg first (see QUICKSTART.md)
pip install -r requirements.txt
python setup.py  # Verify installation
```

### 2. Generate
```bash
python main.py \
  --photo_path "photo.jpg" \
  --topic "Your historical topic in 1-2 sentences" \
  --style_template documentary \
  --voice_profile documentary_female \
  --duration_seconds 10
```

### 3. Output
Check `output/` directory for:
- `*_video.mp4` - Your video
- `*_speech.wav` - Audio narration
- `*_text.txt` - Speech transcript
- `*_subtitles.srt` - Subtitles
- `*_metadata.json` - Generation details

## Use Cases

### Educational Content
- Historical documentaries for classrooms
- Museum exhibits with narrated photos
- Online educational videos
- Academic presentations

### Historical Preservation
- Narrating archival photographs
- Creating context for historical images
- Educational museum installations

### Language Learning
- Multi-language historical content
- Listening comprehension exercises
- Cultural education materials

## Technical Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| TTS | edge-tts | Neural voice synthesis |
| Video | moviepy | Video composition |
| Image | Pillow (PIL) | Image processing |
| Audio | pydub | Audio manipulation |
| Subtitles | srt | SRT file generation |
| Config | PyYAML | Configuration parsing |
| Backend | FFmpeg | Media encoding/decoding |

## Ethical Guidelines

### ✅ DO
- Use for educational purposes
- Label all content as synthetic
- Respect photo copyrights
- Focus on historical facts
- Generate educational narratives

### ❌ DON'T
- Clone real people's voices
- Create misleading content
- Spread disinformation
- Violate photo copyrights
- Circumvent safety filters
- Generate propaganda

## Safety Features

### Input Filtering
The system automatically blocks:
- Violence incitement
- Hate speech
- Instructions for illegal activities
- Extreme political violence

### Output Labeling
All videos include:
- On-screen disclaimer overlay
- Text file disclaimer
- Metadata ethics statement

### Transparency
Every generation logs:
- Timestamp
- Input parameters
- Models used
- Content filtering status

## Examples

### Example 1: English Documentary
```bash
python main.py \
  --photo_path "liberation.jpg" \
  --topic "The liberation of Paris marked a turning point in World War II" \
  --language en \
  --style_template documentary \
  --voice_profile documentary_female \
  --duration_seconds 12
```

Output: Engaging documentary-style narration with warm female voice

### Example 2: Spanish Newsreel
```bash
python main.py \
  --photo_path "industria.jpg" \
  --topic "La revolución industrial transformó profundamente la sociedad" \
  --language es \
  --style_template authoritarian \
  --voice_profile deep_male_retro \
  --duration_seconds 10
```

Output: 1940s-style newsreel with deep male voice and vintage effects

### Example 3: Ukrainian Academic
```bash
python main.py \
  --photo_path "history.jpg" \
  --topic "Історичний аналіз соціальних змін у післявоєнний період" \
  --language uk \
  --style_template lecture \
  --voice_profile authoritative_male \
  --duration_seconds 15
```

Output: Academic lecture style with thoughtful pacing

## Performance

| Video Length | Generation Time | Output Size |
|-------------|-----------------|-------------|
| 5 seconds | ~10-15 sec | ~2-3 MB |
| 10 seconds | ~15-25 sec | ~4-6 MB |
| 20 seconds | ~30-45 sec | ~8-12 MB |

*Times vary based on hardware and complexity*

## Customization

### Voice Parameters
Edit `config.yaml`:
```yaml
voice_profiles:
  custom_voice:
    pitch: -15     # Hz offset (-20 to +20)
    speed: 0.95    # Multiplier (0.8 to 1.2)
    reverb: 0.25   # Reverb amount (0.0 to 0.5)
```

### Video Effects
Modify `video_composer.py` for custom:
- Color grading
- Motion effects
- Transition styles
- Overlay designs

### Speech Patterns
Edit templates in `speech_generator.py` for custom:
- Sentence structures
- Pause patterns
- Rhetorical devices

## Troubleshooting

| Issue | Solution |
|-------|----------|
| FFmpeg not found | Install FFmpeg and add to PATH |
| Module import error | `pip install -r requirements.txt` |
| Content blocked | Revise topic to focus on educational facts |
| Audio/video desync | Adjust `duration_seconds` parameter |
| Poor video quality | Use higher resolution input photos |

## Roadmap

### Planned Features
- [ ] More languages (French, German, Japanese, etc.)
- [ ] Advanced emotion control in speech
- [ ] Custom music background tracks
- [ ] Batch processing multiple photos
- [ ] Web interface
- [ ] REST API
- [ ] Video timeline editor

### Community Contributions
We welcome contributions that:
- Add new languages
- Improve effects
- Enhance safety filters
- Fix bugs
- Improve documentation

## Documentation

| Document | Purpose |
|----------|---------|
| `README.md` | Main documentation, features, usage |
| `QUICKSTART.md` | Fast setup and first video |
| `ARCHITECTURE.md` | Technical details, architecture |
| `PROJECT_SUMMARY.md` | This file - overview |
| `LICENSE` | MIT license + ethics notice |

## Support & Resources

### Getting Help
1. Check `README.md` for detailed documentation
2. Run `python setup.py` to verify installation
3. Run `python test_installation.py` to test components
4. Try `python example_usage.py 1` for working example

### Learning More
- Read `ARCHITECTURE.md` for technical details
- Explore `config.yaml` for customization options
- Review `example_usage.py` for code examples

## License

MIT License with **Ethical Use Notice**

- ✅ Free to use, modify, distribute
- ✅ Must include original license
- ⚠️ Must use ethically and responsibly
- ⚠️ Must label synthetic content
- ⚠️ Educational purposes only

See `LICENSE` file for full details.

## Disclaimer

This software generates **SYNTHETIC CONTENT ONLY**:

🔹 Voices are synthetic neural networks, NOT clones of real people  
🔹 All outputs must be labeled as synthetic  
🔹 Users are responsible for ethical use  
🔹 Users are responsible for photo copyright compliance  
🔹 Intended for educational purposes only  

## Version Information

- **Version**: 1.0.0
- **Release Date**: October 2025
- **Python**: 3.8+
- **Status**: Stable, production-ready

## Credits

### Technologies Used
- Microsoft Edge Neural Voices (via edge-tts)
- MoviePy video library
- Pillow image processing
- FFmpeg multimedia framework

### Developed For
- Educational content creators
- History educators
- Museums and cultural institutions
- Academic researchers

---

**Remember**: Always use responsibly, label as synthetic, and focus on education! 🎓

