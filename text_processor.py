"""
Text processing and tokenization for text statistics.
Handles cleaning and splitting text into words.
"""

import re

class TextProcessor:
    """Processes raw text and extracts words."""
    
    def __init__(self, raw_text):
        """Initialize with raw text content."""
        self.raw_text = raw_text
    
    def get_words(self):
        """Return list of cleaned, lowercase words from text."""
        # Convert to lowercase
        text_lower = self.raw_text.lower()
        
        # Extract only alphabetic words using regex
        words = re.findall(r'[a-z]+', text_lower)
        
        # Remove empty strings and return
        return [word for word in words if word]