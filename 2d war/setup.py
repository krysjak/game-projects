#!/usr/bin/env python3
"""
Setup and installation verification script
"""

import sys
import subprocess
import importlib.util
import os
import shutil
from pathlib import Path


def check_python_version():
    """Check if Python version is adequate"""
    print("Checking Python version...")
    if sys.version_info < (3, 8):
        print("❌ Python 3.8+ required. Current version:", sys.version)
        return False
    print(f"✅ Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")
    return True


def check_ffmpeg():
    """Check if FFmpeg is installed (PATH and common Windows locations)"""
    print("\nChecking FFmpeg...")

    def _try_exec(exec_path: str) -> bool:
        try:
            result = subprocess.run([exec_path, '-version'], capture_output=True, text=True, timeout=5)
            if result.returncode == 0:
                version_line = result.stdout.split('\n')[0]
                print(f"✅ {version_line} ({exec_path})")
                return True
        except Exception:
            return False
        return False

    # 1) Try via PATH
    ffmpeg_in_path = shutil.which('ffmpeg')
    if ffmpeg_in_path and _try_exec(ffmpeg_in_path):
        return True

    # 2) Try WinGet Links directory
    local_appdata = os.environ.get('LOCALAPPDATA', '')
    if local_appdata:
        winget_link = Path(local_appdata) / 'Microsoft' / 'WinGet' / 'Links' / 'ffmpeg.exe'
        if winget_link.exists() and _try_exec(str(winget_link)):
            return True

        # Try scanning WinGet Packages for ffmpeg bins
        winget_pkgs = Path(local_appdata) / 'Microsoft' / 'WinGet' / 'Packages'
        if winget_pkgs.exists():
            for candidate in winget_pkgs.rglob('ffmpeg*/bin/ffmpeg.exe'):
                if candidate.exists() and _try_exec(str(candidate)):
                    return True

    # 3) Common Windows install locations
    common_candidates = [
        r"C:\\ffmpeg\\bin\\ffmpeg.exe",
        r"C:\\Program Files\\ffmpeg\\bin\\ffmpeg.exe",
        r"C:\\Program Files (x86)\\ffmpeg\\bin\\ffmpeg.exe",
    ]
    for c in common_candidates:
        if Path(c).exists() and _try_exec(c):
            return True

    print("❌ FFmpeg not found")
    print("   Tips:")
    print("   - Install from: https://ffmpeg.org/download.html or 'winget install Gyan.FFmpeg'")
    print("   - After installing with WinGet, ensure this directory is in PATH:")
    print("     %LOCALAPPDATA%\\Microsoft\\WinGet\\Links")
    print("   - Or restart your terminal after installation.")
    return False


def check_dependencies():
    """Check if Python dependencies are installed"""
    print("\nChecking Python dependencies...")
    
    required_packages = [
        'PIL',
        'moviepy',
        'pydub',
        'edge_tts',
        'numpy',
        'cv2',
        'srt',
        'yaml'
    ]
    
    missing = []
    installed = []
    
    for package in required_packages:
        package_name = 'Pillow' if package == 'PIL' else package
        package_name = 'opencv-python' if package == 'cv2' else package_name
        package_name = 'pyyaml' if package == 'yaml' else package_name
        
        spec = importlib.util.find_spec(package)
        if spec is None:
            missing.append(package_name)
            print(f"❌ {package_name}")
        else:
            installed.append(package_name)
            print(f"✅ {package_name}")
    
    if missing:
        print(f"\n⚠️  Missing {len(missing)} package(s)")
        print("\nInstall with:")
        print("  pip install -r requirements.txt")
        return False
    
    print(f"\n✅ All {len(installed)} dependencies installed")
    return True


def create_directories():
    """Create necessary directories"""
    print("\nCreating directories...")
    
    import os
    
    directories = ['output', 'examples']
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"✅ {directory}/")
    
    return True


def verify_config():
    """Verify configuration file"""
    print("\nVerifying configuration...")
    
    try:
        import yaml
        with open('config.yaml', 'r') as f:
            config = yaml.safe_load(f)
        
        required_keys = ['voice_profiles', 'style_templates', 'video_effects', 'output']
        for key in required_keys:
            if key not in config:
                print(f"❌ Missing config key: {key}")
                return False
        
        print("✅ config.yaml is valid")
        return True
    except Exception as e:
        print(f"❌ Config error: {e}")
        return False


def main():
    """Run all checks"""
    print("""
╔════════════════════════════════════════════════════════════╗
║     Historical Video Generator - Setup Verification       ║
╚════════════════════════════════════════════════════════════╝
""")
    
    checks = [
        ("Python Version", check_python_version),
        ("FFmpeg", check_ffmpeg),
        ("Dependencies", check_dependencies),
        ("Directories", create_directories),
        ("Configuration", verify_config)
    ]
    
    results = []
    for name, check_func in checks:
        try:
            result = check_func()
            results.append((name, result))
        except Exception as e:
            print(f"❌ {name} check failed: {e}")
            results.append((name, False))
    
    print("\n" + "="*60)
    print("SETUP SUMMARY")
    print("="*60)
    
    all_passed = True
    for name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status} - {name}")
        if not result:
            all_passed = False
    
    print("="*60)
    
    if all_passed:
        print("\n🎉 Setup complete! You're ready to generate videos.")
        print("\nTry running:")
        print("  python example_usage.py 1")
        print("\nOr:")
        print('  python main.py --photo_path "your_photo.jpg" --topic "Your topic" ')
        return 0
    else:
        print("\n⚠️  Please fix the issues above before proceeding.")
        return 1


if __name__ == "__main__":
    sys.exit(main())

