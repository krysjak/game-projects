"""
Subtitle (.srt) generator
"""

import os
from pathlib import Path
import re
import srt
from datetime import timedelta


class SubtitleGenerator:
    """
    Generates SRT subtitle files from text and audio timing
    """
    
    def generate(self, text, audio_path, output_path):
        """
        Generate SRT subtitle file
        
        Args:
            text: The speech text
            audio_path: Path to audio file (to get duration)
            output_path: Where to save .srt file
        """
        
        # Ensure pydub uses a valid ffmpeg/ffprobe (support WinGet installation)
        self._configure_pydub_ffmpeg()

        # Clean text of prosody markers
        clean_text = self._clean_prosody_markers(text)
        
        # Split into sentences
        sentences = self._split_into_sentences(clean_text)
        
        # Get audio duration
        from pydub import AudioSegment
        audio = AudioSegment.from_file(audio_path)
        total_duration = audio.duration_seconds
        
        # Create subtitle entries
        subtitles = []
        time_per_sentence = total_duration / len(sentences)
        
        for i, sentence in enumerate(sentences):
            start = timedelta(seconds=i * time_per_sentence)
            end = timedelta(seconds=(i + 1) * time_per_sentence)
            
            subtitle = srt.Subtitle(
                index=i + 1,
                start=start,
                end=end,
                content=sentence.strip()
            )
            subtitles.append(subtitle)
        
        # Write SRT file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(srt.compose(subtitles))

    def _configure_pydub_ffmpeg(self):
        """Configure pydub to find ffmpeg/ffprobe if not in PATH (Windows WinGet)."""
        try:
            # Determine WinGet ffmpeg paths
            local_appdata = os.environ.get('LOCALAPPDATA')
            if not local_appdata:
                return
            winget_links = Path(local_appdata) / 'Microsoft' / 'WinGet' / 'Links'
            ffmpeg_path = winget_links / 'ffmpeg.exe'
            ffprobe_path = winget_links / 'ffprobe.exe'

            if ffmpeg_path.exists():
                os.environ['FFMPEG_BINARY'] = str(ffmpeg_path)
            if ffprobe_path.exists():
                os.environ['FFPROBE_BINARY'] = str(ffprobe_path)

            from pydub import AudioSegment
            if ffmpeg_path.exists():
                AudioSegment.converter = str(ffmpeg_path)
            if ffprobe_path.exists():
                AudioSegment.ffprobe = str(ffprobe_path)
        except Exception:
            # Best-effort; fall back to defaults
            pass
    
    def _clean_prosody_markers(self, text):
        """Remove prosody markers from text"""
        # Remove [PAUSE=X.Xs] markers
        cleaned = re.sub(r'\[PAUSE=\d+\.?\d*s\]', '', text)
        # Remove multiple spaces
        cleaned = re.sub(r'\s+', ' ', cleaned)
        return cleaned.strip()
    
    def _split_into_sentences(self, text):
        """Split text into sentences"""
        # Simple sentence splitter
        sentences = re.split(r'[.!?]+', text)
        return [s.strip() for s in sentences if s.strip()]

