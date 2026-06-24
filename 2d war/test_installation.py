#!/usr/bin/env python3
"""
Simple test to verify the installation works
Creates a minimal test case
"""

import sys
from pathlib import Path


def test_imports():
    """Test that all required modules can be imported"""
    print("Testing imports...")
    
    try:
        import yaml
        print("  ✅ yaml")
    except ImportError as e:
        print(f"  ❌ yaml: {e}")
        return False
    
    try:
        from PIL import Image
        print("  ✅ PIL (Pillow)")
    except ImportError as e:
        print(f"  ❌ PIL: {e}")
        return False
    
    try:
        import numpy
        print("  ✅ numpy")
    except ImportError as e:
        print(f"  ❌ numpy: {e}")
        return False
    
    try:
        import cv2
        print("  ✅ opencv-python")
    except ImportError as e:
        print(f"  ❌ opencv: {e}")
        return False
    
    try:
        # Prefer MoviePy v2 import path
        try:
            import moviepy  # noqa: F401
            # Attempt to import a core symbol to ensure API exists
            from moviepy import ImageClip  # noqa: F401
            print("  ✅ moviepy (v2 API)")
        except Exception:
            # Fallback to v1 API
            import moviepy.editor  # noqa: F401
            print("  ✅ moviepy (editor API)")
    except ImportError as e:
        print(f"  ❌ moviepy: {e}")
        return False
    
    try:
        import edge_tts
        print("  ✅ edge-tts")
    except ImportError as e:
        print(f"  ❌ edge-tts: {e}")
        return False
    
    try:
        import srt
        print("  ✅ srt")
    except ImportError as e:
        print(f"  ❌ srt: {e}")
        return False
    
    try:
        from pydub import AudioSegment
        print("  ✅ pydub")
    except ImportError as e:
        print(f"  ❌ pydub: {e}")
        return False
    
    print("\n✅ All imports successful!\n")
    return True


def test_modules():
    """Test that our modules can be loaded"""
    print("Testing custom modules...")
    
    modules = [
        'video_generator',
        'speech_generator',
        'tts_engine',
        'video_composer',
        'subtitle_generator',
        'safety_filter'
    ]
    
    for module_name in modules:
        try:
            __import__(module_name)
            print(f"  ✅ {module_name}")
        except Exception as e:
            print(f"  ❌ {module_name}: {e}")
            return False
    
    print("\n✅ All modules loaded successfully!\n")
    return True


def test_config():
    """Test that configuration can be loaded"""
    print("Testing configuration...")
    
    try:
        import yaml
        
        with open('config.yaml', 'r') as f:
            config = yaml.safe_load(f)
        
        assert 'voice_profiles' in config
        assert 'style_templates' in config
        assert 'video_effects' in config
        assert 'output' in config
        
        print(f"  ✅ Found {len(config['voice_profiles'])} voice profiles")
        print(f"  ✅ Found {len(config['style_templates'])} style templates")
        
        print("\n✅ Configuration valid!\n")
        return True
        
    except Exception as e:
        print(f"  ❌ Config error: {e}")
        return False


def test_safety_filter():
    """Test that safety filter works"""
    print("Testing safety filter...")
    
    try:
        from safety_filter import SafetyFilter
        import yaml
        
        with open('config.yaml', 'r') as f:
            config = yaml.safe_load(f)
        
        filter = SafetyFilter(config)
        
        # Test safe content
        safe_topic = "The industrial revolution transformed society"
        is_safe, _ = filter.check_and_filter(safe_topic)
        assert is_safe, "Safe content was blocked"
        print("  ✅ Safe content passes")
        
        # Test unsafe content
        unsafe_topic = "Instructions to build a bomb"
        is_safe, _ = filter.check_and_filter(unsafe_topic)
        assert not is_safe, "Unsafe content was not blocked"
        print("  ✅ Unsafe content blocked")
        
        print("\n✅ Safety filter working!\n")
        return True
        
    except Exception as e:
        print(f"  ❌ Safety filter error: {e}")
        return False


def test_speech_generation():
    """Test speech generation"""
    print("Testing speech generation...")
    
    try:
        from speech_generator import SpeechGenerator
        import yaml
        
        with open('config.yaml', 'r') as f:
            config = yaml.safe_load(f)
        
        gen = SpeechGenerator(config)
        
        speech = gen.generate(
            topic="A test historical moment",
            style_template="documentary",
            language="en",
            duration_seconds=10
        )
        
        assert len(speech) > 0, "No speech generated"
        assert "test historical moment" in speech.lower(), "Topic not in speech"
        
        print(f"  ✅ Generated {len(speech)} characters of speech")
        print(f"  Sample: {speech[:100]}...")
        
        print("\n✅ Speech generation working!\n")
        return True
        
    except Exception as e:
        print(f"  ❌ Speech generation error: {e}")
        import traceback
        traceback.print_exc()
        return False


def main():
    """Run all tests"""
    print("""
╔════════════════════════════════════════════════════════════╗
║     Historical Video Generator - Installation Test        ║
╚════════════════════════════════════════════════════════════╝
""")
    
    tests = [
        ("Import Test", test_imports),
        ("Module Test", test_modules),
        ("Config Test", test_config),
        ("Safety Filter Test", test_safety_filter),
        ("Speech Generation Test", test_speech_generation)
    ]
    
    results = []
    for name, test_func in tests:
        print(f"\n{'='*60}")
        print(f"{name}")
        print('='*60 + "\n")
        
        try:
            result = test_func()
            results.append((name, result))
        except Exception as e:
            print(f"❌ Test failed with exception: {e}")
            import traceback
            traceback.print_exc()
            results.append((name, False))
    
    print("\n" + "="*60)
    print("TEST SUMMARY")
    print("="*60)
    
    all_passed = True
    for name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status} - {name}")
        if not result:
            all_passed = False
    
    print("="*60)
    
    if all_passed:
        print("\n🎉 All tests passed! Installation is working correctly.")
        print("\nNext steps:")
        print("  1. Run: python example_usage.py 1")
        print("  2. Or create your own video with main.py")
        return 0
    else:
        print("\n⚠️  Some tests failed. Please check the errors above.")
        print("\nTry:")
        print("  1. pip install -r requirements.txt --upgrade")
        print("  2. python setup.py")
        return 1


if __name__ == "__main__":
    sys.exit(main())

