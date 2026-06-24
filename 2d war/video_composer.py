"""
Video composition with cinematic effects
"""

import numpy as np
from PIL import Image, ImageDraw, ImageFilter
try:
    # MoviePy v2+ API
    from moviepy import (
        ImageClip, AudioFileClip, CompositeVideoClip,
        TextClip
    )
except Exception:
    # Fallback for MoviePy v1.x
    from moviepy.editor import (
        ImageClip, AudioFileClip, CompositeVideoClip,
        TextClip
    )
try:
    import moviepy.video.fx.all as vfx  # noqa: F401
except Exception:
    vfx = None  # not used currently


class VideoComposer:
    """
    Composes video from photo with effects and audio
    """
    
    def __init__(self, config):
        self.config = config
        self.video_effects = config['video_effects']
        self.output_settings = config['output']
    
    def compose(self, photo_path, audio_path, subtitle_path, style_template,
                duration_seconds, output_path, disclaimer):
        """
        Compose final video with effects
        
        Args:
            photo_path: Path to input photo
            audio_path: Path to audio file
            subtitle_path: Path to subtitle file
            style_template: Style for effects
            duration_seconds: Video duration
            output_path: Where to save video
            disclaimer: Disclaimer text to overlay
        """
        
        # Load and preprocess image
        img = self._preprocess_image(photo_path, style_template)
        
        # Create image clip
        img_clip = ImageClip(img, duration=duration_seconds)
        
        # Apply effects based on style
        img_clip = self._apply_effects(img_clip, style_template)
        
        # Load audio
        audio = AudioFileClip(audio_path)
        
        # Match video duration to audio duration
        actual_duration = audio.duration
        img_clip = img_clip.set_duration(actual_duration)
        
        # Set audio
        video = img_clip.set_audio(audio)
        
        # Add disclaimer overlay
        disclaimer_clip = self._create_disclaimer_overlay(
            disclaimer, actual_duration, 
            self.output_settings['resolution']
        )
        
        # Composite everything
        final = CompositeVideoClip([video, disclaimer_clip])
        
        # Write video file
        final.write_videofile(
            output_path,
            codec=self.output_settings['video_codec'],
            audio_codec=self.output_settings['audio_codec'],
            fps=self.output_settings['fps'],
            preset='medium',
            bitrate='5000k'
        )
        
        # Cleanup
        audio.close()
        final.close()
    
    def _preprocess_image(self, photo_path, style_template):
        """Preprocess image with filters"""
        img = Image.open(photo_path)
        
        # Resize to target resolution
        target_size = tuple(self.output_settings['resolution'])
        
        # Calculate resize to cover (maintain aspect ratio)
        img_ratio = img.width / img.height
        target_ratio = target_size[0] / target_size[1]
        
        if img_ratio > target_ratio:
            # Image is wider
            new_height = target_size[1]
            new_width = int(new_height * img_ratio)
        else:
            # Image is taller
            new_width = target_size[0]
            new_height = int(new_width / img_ratio)
        
        img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
        
        # Center crop
        left = (new_width - target_size[0]) // 2
        top = (new_height - target_size[1]) // 2
        img = img.crop((left, top, left + target_size[0], top + target_size[1]))
        
        # Apply style-specific filters
        if style_template in ['authoritarian', 'documentary']:
            # Vintage/retro effect
            img = self._apply_vintage_effect(img)
        
        return np.array(img)
    
    def _apply_vintage_effect(self, img):
        """Apply vintage/retro effect to image"""
        # Sepia tone
        sepia = self._sepia_tone(img)
        
        # Add grain
        grainy = self._add_grain(sepia)
        
        # Vignette
        vignetted = self._add_vignette(grainy)
        
        # Slight blur for old film look
        vintage = vignetted.filter(ImageFilter.GaussianBlur(0.5))
        
        return vintage
    
    def _sepia_tone(self, img):
        """Apply sepia tone filter"""
        # Convert to grayscale first
        gray = img.convert('L')
        
        # Create sepia image
        sepia = Image.new('RGB', img.size)
        sepia_pixels = []
        
        for pixel in gray.getdata():
            # Sepia formula
            r = int(pixel * 1.0)
            g = int(pixel * 0.95)
            b = int(pixel * 0.82)
            sepia_pixels.append((min(255, r), min(255, g), min(255, b)))
        
        sepia.putdata(sepia_pixels)
        
        # Blend with original
        return Image.blend(img.convert('RGB'), sepia, 0.3)
    
    def _add_grain(self, img):
        """Add film grain effect"""
        img_array = np.array(img)
        noise = np.random.normal(0, 8, img_array.shape)
        grainy = np.clip(img_array + noise, 0, 255).astype(np.uint8)
        return Image.fromarray(grainy)
    
    def _add_vignette(self, img):
        """Add vignette effect"""
        # Create radial gradient mask
        width, height = img.size
        mask = Image.new('L', (width, height), 0)
        draw = ImageDraw.Draw(mask)
        
        # Create elliptical gradient
        for i in range(255, 0, -5):
            intensity = int(i)
            bbox = [
                width * (255 - i) // 510,
                height * (255 - i) // 510,
                width * (255 + i) // 510,
                height * (255 + i) // 510
            ]
            draw.ellipse(bbox, fill=intensity)
        
        # Apply mask
        vignette_layer = Image.new('RGB', img.size, (0, 0, 0))
        return Image.composite(img, vignette_layer, mask)
    
    def _apply_effects(self, clip, style_template):
        """Apply moviepy effects to clip"""
        
        # Ken Burns effect (slow zoom and pan)
        def zoom_pan(t):
            zoom_factor = 1 + 0.1 * (t / clip.duration)
            return zoom_factor
        
        clip = clip.resize(zoom_pan)
        
        # Fade in and out
        clip = clip.fadein(0.5).fadeout(0.5)
        
        return clip
    
    def _create_disclaimer_overlay(self, disclaimer_text, duration, resolution):
        """Create disclaimer text overlay"""
        
        # Create text clip
        txt_clip = TextClip(
            disclaimer_text,
            fontsize=16,
            color='white',
            bg_color='rgba(0,0,0,0.7)',
            font='Arial',
            method='caption',
            size=(resolution[0] - 40, None),
            align='center'
        )
        
        # Position at bottom
        txt_clip = txt_clip.set_position(('center', resolution[1] - 80))
        txt_clip = txt_clip.set_duration(duration)
        
        # Fade in at start, constant visibility
        txt_clip = txt_clip.crossfadein(1.0)
        
        return txt_clip

