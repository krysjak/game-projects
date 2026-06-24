"""
Text-to-Speech engine using edge-tts (offline-capable after initial download)
"""

import asyncio
import re
from pathlib import Path
import edge_tts


class TTSEngine:
    """
    Handles text-to-speech conversion with voice profiles
    """
    
    def __init__(self, config):
        self.config = config
        self.voice_profiles = config['voice_profiles']
    
    def generate(self, text, voice_profile, language, output_path):
        """
        Generate speech audio from text
        
        Args:
            text: Text to convert to speech
            voice_profile: Voice profile name
            language: Language code
            output_path: Where to save the audio file
        """
        
        # Get voice configuration
        voice_config = self.voice_profiles.get(voice_profile, 
                                               self.voice_profiles['neutral_female'])
        
        # Map language to appropriate voice
        voice_id = self._get_voice_for_language(voice_config['voice_id'], language)
        
        # Clean text of prosody markers for edge-tts
        # edge-tts supports SSML, so we'll convert our markers
        ssml_text = self._convert_to_ssml(text, voice_config)
        
        # Generate audio
        asyncio.run(self._async_generate(ssml_text, voice_id, output_path, voice_config))
    
    def _get_voice_for_language(self, base_voice_id, language):
        """Map voice to appropriate language variant"""
        voice_mapping = {
            'en': {
                'en-US-GuyNeural': 'en-US-GuyNeural',
                'en-US-JennyNeural': 'en-US-JennyNeural',
                'en-GB-RyanNeural': 'en-GB-RyanNeural',
                'en-US-AriaNeural': 'en-US-AriaNeural'
            },
            'es': {
                'en-US-GuyNeural': 'es-ES-AlvaroNeural',
                'en-US-JennyNeural': 'es-ES-ElviraNeural',
                'en-GB-RyanNeural': 'es-MX-JorgeNeural',
                'en-US-AriaNeural': 'es-ES-AbrilNeural'
            },
            'uk': {
                'en-US-GuyNeural': 'uk-UA-OstapNeural',
                'en-US-JennyNeural': 'uk-UA-PolinaNeural',
                'en-GB-RyanNeural': 'uk-UA-OstapNeural',
                'en-US-AriaNeural': 'uk-UA-PolinaNeural'
            }
        }
        
        lang_voices = voice_mapping.get(language, voice_mapping['en'])
        return lang_voices.get(base_voice_id, base_voice_id)
    
    def _convert_to_ssml(self, text, voice_config):
        """Convert our pause markers to SSML breaks"""
        # Remove our custom pause markers and replace with SSML breaks
        ssml = text
        
        # Replace [PAUSE=X.Xs] with SSML breaks
        ssml = re.sub(r'\[PAUSE=(\d+\.?\d*)s\]', 
                     r'<break time="\1s"/>', ssml)
        
        return ssml
    
    async def _async_generate(self, text, voice_id, output_path, voice_config):
        """Async generation using edge-tts"""
        
        # Create communicate object
        rate_percent = int((voice_config['speed'] - 1.0) * 100)
        # edge-tts expects a signed percentage string (e.g., +0%, +10%, -5%)
        rate_str = f"{rate_percent:+d}%"
        communicate = edge_tts.Communicate(
            text=text,
            voice=voice_id,
            rate=rate_str,
            pitch=f"{voice_config['pitch']:+d}Hz"
        )
        
        # Save to file
        await communicate.save(output_path)
    
    def get_model_info(self):
        """Return information about the TTS model"""
        return {
            "engine": "edge-tts",
            "version": edge_tts.__version__ if hasattr(edge_tts, '__version__') else "latest",
            "type": "neural_voices",
            "note": "Uses Microsoft Edge Neural Voices (synthetic, not cloned)"
        }

