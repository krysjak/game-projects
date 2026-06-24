"""
Safety filter to block harmful content
"""

import re


class SafetyFilter:
    """
    Filters content for violence, hate speech, and illegal activity
    """
    
    def __init__(self, config):
        self.config = config
        self.blocked_patterns = self._compile_patterns()
    
    def _compile_patterns(self):
        """Compile regex patterns for blocked content"""
        patterns = [
            # Violence incitement
            r'\b(kill|murder|attack|destroy|annihilate|exterminate)\s+(all|the)\s+',
            r'\b(genocide|massacre|slaughter)\b',
            r'\bcall\s+to\s+(arms|violence)\b',
            
            # Hate speech
            r'\b(inferior|subhuman|vermin)\s+(race|people|group)\b',
            r'\bethnic\s+cleansing\b',
            r'\bfinal\s+solution\b',
            
            # Illegal activity promotion
            r'\b(how\s+to|instructions?\s+(to|for))\s+(make|build|create|assemble)\s+(a\s+)?(bomb|weapon|explosive|pipe\s*bomb|molotov)\b',
            r'\b(smuggle|trafficking|illegal\s+trade)\b',
            
            # Extreme political violence
            r'\b(overthrow|assassinate|coup)\s+(government|leader|president)\b',
        ]
        
        return [re.compile(pattern, re.IGNORECASE) for pattern in patterns]
    
    def check_and_filter(self, text):
        """
        Check text for prohibited content
        
        Args:
            text: Input text to check
        
        Returns:
            tuple: (is_safe: bool, filtered_text: str)
        """
        
        # Check against patterns
        for pattern in self.blocked_patterns:
            if pattern.search(text):
                return False, text
        
        # Check for excessive profanity or extreme language
        extreme_words = [
            'annihilate', 'exterminate', 'eradicate',
            'purge', 'cleanse', 'eliminate'
        ]
        
        text_lower = text.lower()
        extreme_count = sum(1 for word in extreme_words if word in text_lower)
        
        if extreme_count > 2:
            return False, text
        
        # Mild filtering - replace extreme language with educational language
        filtered = text
        replacements = {
            r'\b(conquer|dominated)\b': 'occupied',
            r'\b(crushed|destroyed)\b': 'defeated',
            r'\bsubjugated\b': 'controlled'
        }
        
        for pattern, replacement in replacements.items():
            filtered = re.sub(pattern, replacement, filtered, flags=re.IGNORECASE)
        
        return True, filtered

