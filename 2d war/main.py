#!/usr/bin/env python3
"""
Historical Video Generator - Offline Agent
Generates educational historical videos with synthetic speech and effects.
"""

import argparse
import sys
from pathlib import Path
from video_generator import HistoricalVideoGenerator


def main():
    parser = argparse.ArgumentParser(
        description='Generate educational historical videos with synthetic speech'
    )
    
    parser.add_argument('--photo_path', required=True, help='Path to input photo')
    parser.add_argument('--topic', required=True, help='Speech topic (1-2 sentences)')
    parser.add_argument('--language', default='en', 
                       choices=['en', 'es', 'uk'], 
                       help='Language code')
    parser.add_argument('--voice_profile', default='neutral_female',
                       choices=['deep_male_retro', 'neutral_female', 
                               'authoritative_male', 'documentary_female'],
                       help='Voice profile to use')
    parser.add_argument('--style_template', default='documentary',
                       choices=['authoritarian', 'documentary', 
                               'neutral_narrator', 'lecture'],
                       help='Speech style template')
    parser.add_argument('--duration_seconds', type=int, default=10,
                       help='Desired video length (2-20 seconds)')
    parser.add_argument('--output_dir', default='output',
                       help='Output directory')
    
    args = parser.parse_args()
    
    # Validate inputs
    if not Path(args.photo_path).exists():
        print(f"Error: Photo not found at {args.photo_path}")
        sys.exit(1)
    
    if not (2 <= args.duration_seconds <= 20):
        print("Error: duration_seconds must be between 2 and 20")
        sys.exit(1)
    
    # Create generator
    generator = HistoricalVideoGenerator()
    
    # Generate video
    try:
        result = generator.generate(
            photo_path=args.photo_path,
            topic=args.topic,
            language=args.language,
            voice_profile=args.voice_profile,
            style_template=args.style_template,
            duration_seconds=args.duration_seconds,
            output_dir=args.output_dir
        )
        
        print("\n" + "="*60)
        print("VIDEO GENERATION COMPLETED SUCCESSFULLY")
        print("="*60)
        print(f"\nOutputs generated in: {result['output_dir']}")
        print(f"  - Speech text: {result['text_file']}")
        print(f"  - Audio file: {result['audio_file']}")
        print(f"  - Video file: {result['video_file']}")
        print(f"  - Subtitles: {result['subtitle_file']}")
        print(f"  - Metadata: {result['metadata_file']}")
        print(f"\nDisclaimer: {result['disclaimer']}")
        
    except Exception as e:
        print(f"\nError during generation: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()

