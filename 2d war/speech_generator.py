"""
Speech text generator with style templates
"""

import re


class SpeechGenerator:
    """
    Generates speech text based on topic and style template
    """
    
    def __init__(self, config):
        self.config = config
        self.style_templates = config['style_templates']
    
    def generate(self, topic, style_template, language, duration_seconds):
        """
        Generate speech text based on parameters
        
        Args:
            topic: The subject matter
            style_template: Style to apply
            language: Language code
            duration_seconds: Target duration
        
        Returns:
            str: Generated speech text with prosody markers
        """
        
        style = self.style_templates.get(style_template, 
                                         self.style_templates['neutral_narrator'])
        
        # Estimate words needed (average speaking rate: 150 words/min)
        target_words = int((duration_seconds / 60) * 150)
        
        # Generate speech based on style
        if style_template == 'authoritarian':
            speech = self._generate_authoritarian(topic, target_words, language)
        elif style_template == 'documentary':
            speech = self._generate_documentary(topic, target_words, language)
        elif style_template == 'lecture':
            speech = self._generate_lecture(topic, target_words, language)
        else:  # neutral_narrator
            speech = self._generate_neutral(topic, target_words, language)
        
        # Add prosody hints based on pause pattern
        speech = self._add_prosody_hints(speech, style['pause_pattern'])
        
        return speech
    
    def _generate_authoritarian(self, topic, target_words, language):
        """Generate authoritarian style speech"""
        templates = {
            'en': [
                f"Attention! {topic}",
                f"[PAUSE=0.6s] This is what you must know.",
                f"[PAUSE=0.4s] Remember this.",
                f"[PAUSE=0.6s] History demands it."
            ],
            'es': [
                f"¡Atención! {topic}",
                f"[PAUSE=0.6s] Esto es lo que debes saber.",
                f"[PAUSE=0.4s] Recuerda esto.",
                f"[PAUSE=0.6s] La historia lo exige."
            ],
            'uk': [
                f"Увага! {topic}",
                f"[PAUSE=0.6s] Це те, що ви повинні знати.",
                f"[PAUSE=0.4s] Запам'ятайте це.",
                f"[PAUSE=0.6s] Історія вимагає цього."
            ]
        }
        
        lines = templates.get(language, templates['en'])
        return ' '.join(lines[:self._estimate_sentences(target_words)])
    
    def _generate_documentary(self, topic, target_words, language):
        """Generate documentary style speech"""
        templates = {
            'en': [
                f"In the annals of history, {topic.lower()}",
                f"[PAUSE=0.3s] What we see here tells a remarkable story.",
                f"[PAUSE=0.3s] A story that continues to resonate today.",
                f"[PAUSE=0.4s] Through this image, we glimpse the past."
            ],
            'es': [
                f"En los anales de la historia, {topic.lower()}",
                f"[PAUSE=0.3s] Lo que vemos aquí cuenta una historia notable.",
                f"[PAUSE=0.3s] Una historia que sigue resonando hoy.",
                f"[PAUSE=0.4s] A través de esta imagen, vislumbramos el pasado."
            ],
            'uk': [
                f"В анналах історії, {topic.lower()}",
                f"[PAUSE=0.3s] Те, що ми бачимо тут, розповідає чудову історію.",
                f"[PAUSE=0.3s] Історію, яка продовжує резонувати сьогодні.",
                f"[PAUSE=0.4s] Крізь це зображення ми glimpse минуле."
            ]
        }
        
        lines = templates.get(language, templates['en'])
        return ' '.join(lines[:self._estimate_sentences(target_words)])
    
    def _generate_lecture(self, topic, target_words, language):
        """Generate lecture style speech"""
        templates = {
            'en': [
                f"Let us examine {topic.lower()}",
                f"[PAUSE=0.5s] From an academic perspective, this represents a significant moment.",
                f"[PAUSE=0.3s] We can analyze several key elements here.",
                f"[PAUSE=0.5s] Consider the broader historical context."
            ],
            'es': [
                f"Examinemos {topic.lower()}",
                f"[PAUSE=0.5s] Desde una perspectiva académica, esto representa un momento significativo.",
                f"[PAUSE=0.3s] Podemos analizar varios elementos clave aquí.",
                f"[PAUSE=0.5s] Considera el contexto histórico más amplio."
            ],
            'uk': [
                f"Давайте розглянемо {topic.lower()}",
                f"[PAUSE=0.5s] З академічної точки зору, це є значущим моментом.",
                f"[PAUSE=0.3s] Ми можемо проаналізувати кілька ключових елементів тут.",
                f"[PAUSE=0.5s] Розгляньте ширший історичний контекст."
            ]
        }
        
        lines = templates.get(language, templates['en'])
        return ' '.join(lines[:self._estimate_sentences(target_words)])
    
    def _generate_neutral(self, topic, target_words, language):
        """Generate neutral narrator style speech"""
        templates = {
            'en': [
                f"{topic}",
                f"[PAUSE=0.3s] This image captures an important historical moment.",
                f"[PAUSE=0.3s] It serves as a window into the past.",
                f"[PAUSE=0.3s] Providing valuable insight into that era."
            ],
            'es': [
                f"{topic}",
                f"[PAUSE=0.3s] Esta imagen captura un momento histórico importante.",
                f"[PAUSE=0.3s] Sirve como una ventana al pasado.",
                f"[PAUSE=0.3s] Proporciona información valiosa sobre esa época."
            ],
            'uk': [
                f"{topic}",
                f"[PAUSE=0.3s] Це зображення фіксує важливий історичний момент.",
                f"[PAUSE=0.3s] Воно служить вікном у минуле.",
                f"[PAUSE=0.3s] Надає цінне розуміння тієї епохи."
            ]
        }
        
        lines = templates.get(language, templates['en'])
        return ' '.join(lines[:self._estimate_sentences(target_words)])
    
    def _estimate_sentences(self, target_words):
        """Estimate number of sentences needed"""
        # Average 15 words per sentence
        return max(2, min(4, target_words // 15))
    
    def _add_prosody_hints(self, text, pause_pattern):
        """Add additional prosody markers based on pattern"""
        # Already includes PAUSE markers from templates
        # Add period pauses
        text = re.sub(r'\.(?!\])', '.[PAUSE=0.2s]', text)
        text = re.sub(r',', ',[PAUSE=0.1s]', text)
        
        return text

