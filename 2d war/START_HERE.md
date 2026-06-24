# 🎬 Historical Video Generator - START HERE

Welcome! This file will get you up and running in **less than 10 minutes**.

## What You're About to Build

Transform a single photo into a professional educational video with:
- 🎙️ Synthetic AI narration (English, Spanish, or Ukrainian)
- 🎨 Cinematic vintage effects
- 📝 Auto-generated subtitles
- ⚡ Multiple voice and style options

**Example Output**: A 10-second video with documentary narration over a historical photo with vintage film effects.

---

## ⚡ 5-Minute Quick Start

### Step 1: Install FFmpeg (2 minutes)

**Windows:**
1. Download from https://ffmpeg.org/download.html
2. Extract to `C:\ffmpeg`
3. Add `C:\ffmpeg\bin` to System PATH
4. Restart your terminal

**Linux:**
```bash
sudo apt-get update && sudo apt-get install ffmpeg
```

**macOS:**
```bash
brew install ffmpeg
```

Verify installation:
```bash
ffmpeg -version
```

### Step 2: Install Python Packages (2 minutes)

```bash
pip install -r requirements.txt
```

### Step 3: Verify Setup (1 minute)

```bash
python setup.py
```

You should see ✅ for all checks. If any ❌ appear, follow the displayed instructions.

### Step 4: Generate Your First Video! (30 seconds)

```bash
python example_usage.py 1
```

This creates a sample photo and generates a documentary-style video.

**Check your output:** Look in `output/example1/` for `*_video.mp4`

---

## 🎯 Next: Use Your Own Photo

```bash
python main.py ^
  --photo_path "C:\path\to\your\photo.jpg" ^
  --topic "A pivotal moment in World War II history" ^
  --style_template documentary ^
  --voice_profile documentary_female ^
  --duration_seconds 10
```

**Linux/Mac users:** Replace `^` with `\` for line continuation.

---

## 🎨 Try Different Styles

### Documentary Style (Engaging Narrator)
```bash
python main.py ^
  --photo_path "photo.jpg" ^
  --topic "The fall of the Berlin Wall marked the end of an era" ^
  --style_template documentary ^
  --voice_profile documentary_female ^
  --duration_seconds 12
```

### 1940s Newsreel Style (Authoritative)
```bash
python main.py ^
  --photo_path "photo.jpg" ^
  --topic "Workers unite for progress and prosperity" ^
  --style_template authoritarian ^
  --voice_profile deep_male_retro ^
  --duration_seconds 8
```

### Academic Lecture Style
```bash
python main.py ^
  --photo_path "photo.jpg" ^
  --topic "Examining the social transformations of the twentieth century" ^
  --style_template lecture ^
  --voice_profile authoritative_male ^
  --duration_seconds 15
```

---

## 🗣️ Available Voices

| Voice Profile | Description | Best For |
|---------------|-------------|----------|
| `documentary_female` | Warm, engaging | Modern documentaries |
| `deep_male_retro` | Deep, reverb-heavy | 1940s newsreels |
| `authoritative_male` | British-accented | Academic content |
| `neutral_female` | Clear, objective | General narration |

## 🎭 Available Styles

| Style | Characteristics | Example |
|-------|----------------|---------|
| `documentary` | Engaging, narrative | "In the annals of history..." |
| `authoritarian` | Commanding, emphatic | "Attention! Remember this!" |
| `neutral_narrator` | Objective, clear | "This image captures..." |
| `lecture` | Analytical, thoughtful | "Let us examine..." |

## 🌍 Languages

- `--language en` - English (default)
- `--language es` - Spanish (Español)
- `--language uk` - Ukrainian (Українська)

---

## 📁 Output Files

Each generation creates 5 files:

```
output/
  video_20241015_143022_text.txt        # Speech transcript
  video_20241015_143022_speech.wav      # Audio narration
  video_20241015_143022_video.mp4       # ⭐ FINAL VIDEO ⭐
  video_20241015_143022_subtitles.srt   # Subtitle file
  video_20241015_143022_metadata.json   # Generation details
```

---

## ⚙️ All Command Options

```bash
python main.py \
  --photo_path "path/to/photo.jpg"        # Required: Your photo
  --topic "Your topic description"        # Required: What to say
  --language en                           # Optional: en/es/uk
  --voice_profile documentary_female      # Optional: See voices above
  --style_template documentary            # Optional: See styles above
  --duration_seconds 10                   # Optional: 2-20 seconds
  --output_dir output                     # Optional: Output folder
```

---

## ❗ Troubleshooting

### "FFmpeg not found"
- Windows: Check PATH includes `C:\ffmpeg\bin`
- Restart terminal after installing FFmpeg
- Test with: `ffmpeg -version`

### "Module not found"
```bash
pip install -r requirements.txt --upgrade
```

### "Content blocked by safety filter"
Your topic contains prohibited content (violence, hate speech, etc.)

**Fix**: Rewrite topic to focus on educational facts:
- ❌ "Instructions to attack enemies"
- ✅ "Historical analysis of military strategy"

### "Audio/video out of sync"
Adjust `--duration_seconds` to match your topic length:
- Short topics: 5-8 seconds
- Medium topics: 10-15 seconds
- Long topics: 15-20 seconds

### "Poor video quality"
Use higher resolution photos (1920x1080 or larger recommended)

---

## 🛡️ Ethics & Safety

### This System:
✅ Uses **synthetic voices only** (NOT cloned from real people)  
✅ Processes **static images only** (NO deepfakes)  
✅ Includes **mandatory disclaimers** on all videos  
✅ **Filters harmful content** automatically  
✅ Designed for **educational use only**  

### Your Responsibilities:
⚠️ Always label content as "AI-generated" or "Synthetic"  
⚠️ Use only photos you have rights to  
⚠️ Use for education, not misinformation  
⚠️ Don't create content impersonating real people  
⚠️ Follow all applicable laws  

---

## 📚 Learn More

- **[README.md](README.md)** - Complete documentation
- **[QUICKSTART.md](QUICKSTART.md)** - Detailed setup guide
- **[DOCS_INDEX.md](DOCS_INDEX.md)** - Find any documentation
- **[ARCHITECTURE.md](ARCHITECTURE.md)** - How it works (developers)
- **[config.yaml](config.yaml)** - Customize voices and effects

---

## 🎓 Example Projects

### History Classroom
Generate videos for historical photos with educational narration.

### Museum Exhibit
Create narrated slideshows for archival photographs.

### Language Learning
Produce listening comprehension materials in multiple languages.

### Academic Research
Illustrate historical research with narrated visuals.

---

## ✅ Success Checklist

After following this guide, you should be able to:

- [x] Install all dependencies
- [x] Verify installation with `setup.py`
- [x] Generate example video with `example_usage.py 1`
- [x] Create video from your own photo
- [x] Understand voice and style options
- [x] Troubleshoot common issues
- [x] Use the system ethically

---

## 🚀 You're Ready!

**Congratulations!** You now have a complete video generation system.

**Next Steps:**
1. Generate a few test videos with different styles
2. Experiment with voice profiles
3. Try different languages
4. Read [README.md](README.md) for advanced features
5. Customize [config.yaml](config.yaml) for your needs

---

## 💡 Pro Tips

1. **Better Photos = Better Videos**: Use high-res images (1920x1080+)
2. **Match Duration to Content**: Longer topics need more seconds
3. **Test Different Voices**: Each voice has unique character
4. **Batch Processing**: Generate multiple videos, then review
5. **Keep Topics Concise**: 1-2 sentences work best

---

## 🎬 Happy Creating!

You're all set to create professional educational videos. Remember to:
- Use responsibly
- Label as synthetic
- Focus on education
- Have fun! 🎉

**Questions?** Check [DOCS_INDEX.md](DOCS_INDEX.md) for complete documentation guide.

---

Made with ❤️ for education | [MIT License](LICENSE) | Version 1.0.0

