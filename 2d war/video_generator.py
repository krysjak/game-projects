"""
Main video generator orchestrator
"""

import json
from pathlib import Path
from datetime import datetime
import yaml

from speech_generator import SpeechGenerator
from tts_engine import TTSEngine
from video_composer import VideoComposer
from subtitle_generator import SubtitleGenerator
from safety_filter import SafetyFilter


class HistoricalVideoGenerator:
    """
    Orchestrates the entire video generation pipeline
    """
    
    DISCLAIMER = "Synthetic content. Not an authentic speech by any real person."
    
    def __init__(self, config_path='config.yaml'):
        """Initialize with configuration"""
        with open(config_path, 'r', encoding='utf-8') as f:
            self.config = yaml.safe_load(f)
        
        self.speech_gen = SpeechGenerator(self.config)
        self.tts_engine = TTSEngine(self.config)
        self.video_composer = VideoComposer(self.config)
        self.subtitle_gen = SubtitleGenerator()
        self.safety_filter = SafetyFilter(self.config)
    
    def generate(self, photo_path, topic, language, voice_profile, 
                 style_template, duration_seconds, output_dir='output'):
        """
        Generate complete video package
        
        Args:
            photo_path: Path to input photo
            topic: Speech topic description
            language: Language code (en/es/uk)
            voice_profile: Voice profile name
            style_template: Style template name
            duration_seconds: Target video duration
            output_dir: Output directory
        
        Returns:
            dict with paths to all generated files
        """
        
        # Create output directory
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        base_name = f"video_{timestamp}"
        
        print(f"\n{'='*60}")
        print(f"HISTORICAL VIDEO GENERATOR - OFFLINE AGENT")
        print(f"{'='*60}\n")
        
        # Step 1: Safety check
        print("[1/6] Running safety filter...")
        is_safe, filtered_topic = self.safety_filter.check_and_filter(topic)
        if not is_safe:
            raise ValueError(
                f"Content blocked by safety filter. "
                f"The requested topic contains prohibited content "
                f"(violence incitement, hate speech, or illegal activities)."
            )
        
        # Step 2: Generate speech text
        print("[2/6] Generating speech text...")
        speech_text = self.speech_gen.generate(
            topic=filtered_topic,
            style_template=style_template,
            language=language,
            duration_seconds=duration_seconds
        )
        
        # Save speech text
        text_file = output_path / f"{base_name}_text.txt"
        with open(text_file, 'w', encoding='utf-8') as f:
            f.write(f"{self.DISCLAIMER}\n\n")
            f.write(speech_text)
        print(f"   Saved: {text_file}")
        
        # Step 3: Generate TTS audio
        print("[3/6] Generating speech audio...")
        audio_file = output_path / f"{base_name}_speech.wav"
        self.tts_engine.generate(
            text=speech_text,
            voice_profile=voice_profile,
            language=language,
            output_path=str(audio_file)
        )
        print(f"   Saved: {audio_file}")
        
        # Step 4: Generate subtitles
        print("[4/6] Generating subtitles...")
        subtitle_file = output_path / f"{base_name}_subtitles.srt"
        self.subtitle_gen.generate(
            text=speech_text,
            audio_path=str(audio_file),
            output_path=str(subtitle_file)
        )
        print(f"   Saved: {subtitle_file}")
        
        # Step 5: Generate video
        print("[5/6] Composing video with effects...")
        video_file = output_path / f"{base_name}_video.mp4"
        self.video_composer.compose(
            photo_path=photo_path,
            audio_path=str(audio_file),
            subtitle_path=str(subtitle_file),
            style_template=style_template,
            duration_seconds=duration_seconds,
            output_path=str(video_file),
            disclaimer=self.DISCLAIMER
        )
        print(f"   Saved: {video_file}")
        
        # Step 6: Generate metadata
        print("[6/6] Creating metadata...")
        metadata = {
            "timestamp": timestamp,
            "datetime": datetime.now().isoformat(),
            "inputs": {
                "photo_path": str(photo_path),
                "topic": filtered_topic,
                "language": language,
                "voice_profile": voice_profile,
                "style_template": style_template,
                "duration_seconds": duration_seconds
            },
            "outputs": {
                "text_file": str(text_file.name),
                "audio_file": str(audio_file.name),
                "video_file": str(video_file.name),
                "subtitle_file": str(subtitle_file.name)
            },
            "models": {
                "tts_engine": self.tts_engine.get_model_info(),
                "speech_generator": "rule-based template system v1.0"
            },
            "disclaimer": self.DISCLAIMER,
            "ethics_note": "This content was generated using synthetic voices and does not clone any real person's voice or likeness.",
            "safety_filter": "enabled",
            "content_filtered": filtered_topic != topic
        }
        
        metadata_file = output_path / f"{base_name}_metadata.json"
        with open(metadata_file, 'w', encoding='utf-8') as f:
            json.dump(metadata, f, indent=2, ensure_ascii=False)
        print(f"   Saved: {metadata_file}")
        
        print(f"\n{'='*60}")
        
        return {
            "output_dir": str(output_path),
            "text_file": str(text_file.name),
            "audio_file": str(audio_file.name),
            "video_file": str(video_file.name),
            "subtitle_file": str(subtitle_file.name),
            "metadata_file": str(metadata_file.name),
            "disclaimer": self.DISCLAIMER
        }

