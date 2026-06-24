# Documentation Index

Welcome to the Historical Video Generator documentation! This guide will help you find the information you need.

## 📚 Documentation Files

### For New Users

1. **[QUICKSTART.md](QUICKSTART.md)** ⭐ START HERE
   - Installation steps
   - Your first video in 5 minutes
   - Basic commands and examples
   - Troubleshooting common issues

2. **[README.md](README.md)** 📖 MAIN DOCUMENTATION
   - Complete feature overview
   - Detailed usage instructions
   - All command-line options
   - Examples for all styles and voices
   - Configuration guide
   - Full troubleshooting section

3. **[PROJECT_SUMMARY.md](PROJECT_SUMMARY.md)** 📋 OVERVIEW
   - Project purpose and goals
   - Key features summary
   - Use cases and examples
   - Ethics and safety guidelines
   - Quick reference tables

### For Developers

4. **[ARCHITECTURE.md](ARCHITECTURE.md)** 🏗️ TECHNICAL DEEP DIVE
   - System architecture diagrams
   - Module descriptions
   - Data flow and pipelines
   - API documentation
   - Extension guide
   - Performance notes

5. **[LICENSE](LICENSE)** ⚖️ LEGAL & ETHICS
   - MIT License terms
   - Ethical use requirements
   - Restrictions and responsibilities

### Configuration & Code

6. **[config.yaml](config.yaml)** ⚙️ CONFIGURATION
   - Voice profiles
   - Style templates
   - Video effects settings
   - Output parameters

7. **[requirements.txt](requirements.txt)** 📦 DEPENDENCIES
   - Python package list
   - Version requirements

## 🚀 Quick Navigation

### I want to...

#### Get Started
→ Read [QUICKSTART.md](QUICKSTART.md)  
→ Run `python setup.py` to verify installation  
→ Run `python example_usage.py 1` for a demo  

#### Learn All Features
→ Read [README.md](README.md)  
→ Check [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md) for overview  

#### Understand How It Works
→ Read [ARCHITECTURE.md](ARCHITECTURE.md)  
→ Explore the source code with comments  

#### Customize Voices or Styles
→ Edit [config.yaml](config.yaml)  
→ See customization section in [README.md](README.md)  
→ Read module details in [ARCHITECTURE.md](ARCHITECTURE.md)  

#### Troubleshoot Issues
→ Check troubleshooting in [QUICKSTART.md](QUICKSTART.md)  
→ Run `python setup.py` for diagnostics  
→ Run `python test_installation.py` for component tests  

#### Understand Ethics & Safety
→ Read ethics section in [README.md](README.md)  
→ Review [LICENSE](LICENSE) ethical use notice  
→ Check [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md) guidelines  

#### Contribute or Extend
→ Study [ARCHITECTURE.md](ARCHITECTURE.md)  
→ Review module structure  
→ Follow extension guidelines in architecture docs  

## 📖 Reading Order

### For First-Time Users
1. [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md) - Get an overview (5 min)
2. [QUICKSTART.md](QUICKSTART.md) - Install and run (10 min)
3. [README.md](README.md) - Learn all features (20 min)

### For Developers
1. [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md) - Understand the project
2. [ARCHITECTURE.md](ARCHITECTURE.md) - Study the architecture
3. Source code files - Dive into implementation

### For Educators
1. [README.md](README.md) - Features and capabilities
2. [QUICKSTART.md](QUICKSTART.md) - How to create content
3. [LICENSE](LICENSE) - Ethics and legal requirements

## 🛠️ Utility Scripts

### Setup & Testing

- **`setup.py`** - Verify installation and dependencies
  ```bash
  python setup.py
  ```

- **`test_installation.py`** - Run component tests
  ```bash
  python test_installation.py
  ```

- **`example_usage.py`** - Generate example videos
  ```bash
  python example_usage.py 1  # Documentary style
  python example_usage.py 2  # Authoritarian style
  python example_usage.py 3  # Academic style
  ```

### Main Application

- **`main.py`** - Generate custom videos
  ```bash
  python main.py --photo_path "photo.jpg" --topic "Your topic" [options]
  ```

## 📊 Document Comparison

| Document | Length | Audience | Purpose |
|----------|--------|----------|---------|
| QUICKSTART.md | Short | Beginners | Fast setup, first video |
| README.md | Long | All users | Complete reference |
| PROJECT_SUMMARY.md | Medium | All users | Quick overview |
| ARCHITECTURE.md | Long | Developers | Technical details |
| LICENSE | Short | All users | Legal terms |

## 🎯 Common Tasks

### Task: Install the System
1. Read installation section in [QUICKSTART.md](QUICKSTART.md)
2. Install FFmpeg (platform-specific instructions)
3. Run `pip install -r requirements.txt`
4. Run `python setup.py` to verify

### Task: Generate First Video
1. Follow [QUICKSTART.md](QUICKSTART.md) Step 3
2. Use `python example_usage.py 1` for guided demo
3. Check `output/` for results

### Task: Customize Voice
1. Open [config.yaml](config.yaml)
2. Edit voice profile parameters (pitch, speed, reverb)
3. Or select different `voice_id` from edge-tts voices
4. See voice section in [README.md](README.md)

### Task: Add New Style
1. Study style templates in [ARCHITECTURE.md](ARCHITECTURE.md)
2. Add new template to [config.yaml](config.yaml)
3. Implement generation method in `speech_generator.py`
4. Test with `main.py`

### Task: Debug Issues
1. Run `python setup.py` - check dependencies
2. Run `python test_installation.py` - test components
3. Check troubleshooting in [QUICKSTART.md](QUICKSTART.md)
4. Review error messages - safety filter, file I/O, etc.

### Task: Understand Safety Features
1. Read safety section in [README.md](README.md)
2. Review `safety_filter.py` source code
3. See ethical guidelines in [LICENSE](LICENSE)
4. Check [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md) ethics section

## 📞 Getting Help

### Self-Service
1. **Search documentation** - Use Ctrl+F in relevant doc file
2. **Run diagnostics** - `python setup.py`
3. **Run tests** - `python test_installation.py`
4. **Try examples** - `python example_usage.py 1`

### Common Questions

**Q: How do I install?**  
A: See [QUICKSTART.md](QUICKSTART.md) Step 1

**Q: What voices are available?**  
A: See voice profiles in [README.md](README.md) or [config.yaml](config.yaml)

**Q: How do I customize styles?**  
A: Edit [config.yaml](config.yaml), see customization in [README.md](README.md)

**Q: Why was my content blocked?**  
A: Safety filter detected prohibited content. See safety section in [README.md](README.md)

**Q: How does it work technically?**  
A: Read [ARCHITECTURE.md](ARCHITECTURE.md)

**Q: Can I use this commercially?**  
A: See [LICENSE](LICENSE) - MIT license allows commercial use, but follow ethical guidelines

**Q: Is this voice cloning?**  
A: NO. Uses only synthetic neural voices. See ethics section in [README.md](README.md)

## 🔍 Search Tips

Each markdown file is searchable. Use your text editor's search (Ctrl+F) to find:

- **Error messages**: Search in QUICKSTART.md troubleshooting
- **Command options**: Search in README.md usage section
- **Code functions**: Search in ARCHITECTURE.md module descriptions
- **Configuration keys**: Search in config.yaml or ARCHITECTURE.md
- **Ethical guidelines**: Search in LICENSE or README.md

## 📈 Documentation Versions

- **Current Version**: 1.0.0
- **Last Updated**: October 2025
- **Maintained**: Yes
- **Language**: English

## ✅ Documentation Checklist

Use this checklist to verify you understand the system:

- [ ] Installed all dependencies (QUICKSTART.md)
- [ ] Generated first video successfully (QUICKSTART.md)
- [ ] Understand all voice profiles (README.md)
- [ ] Understand all style templates (README.md)
- [ ] Know how to customize settings (config.yaml + README.md)
- [ ] Understand ethical requirements (LICENSE + README.md)
- [ ] Understand safety features (README.md + PROJECT_SUMMARY.md)
- [ ] Can troubleshoot common issues (QUICKSTART.md)
- [ ] Understand technical architecture (ARCHITECTURE.md) [optional for developers]

---

**Still can't find what you need?**  
Try reading in this order:
1. PROJECT_SUMMARY.md (overview)
2. QUICKSTART.md (get started)
3. README.md (complete guide)
4. ARCHITECTURE.md (deep dive)

Happy creating! 🎬

