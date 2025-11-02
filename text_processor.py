"""
Text processing and tokenization for text statistics.
Handles cleaning and splitting text into words.
"""

import re

class TextProcessor:
    """It Processes raw text and extracts clean word list."""
    
    def __init__(self, raw_text):
        """ This Initialize with raw text content."""
        self.raw_text = raw_text
    
    def get_words(self):
        """ It will return list of lowercase alphabetic words."""
        text_lower = self.raw_text.lower()
        words = re.findall(r"[a-z]+", text_lower)
        # Removed empty strings just in case
        cleaned_words = [word for word in words if word]
        return cleaned_words
