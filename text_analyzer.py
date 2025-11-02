"""
Statistical analysis of text data.
Calculates word counts, character counts, and 
frequency statistics.
"""

from collections import Counter

class TextAnalyzer:
    """Analyzes text and generates simple text 
        statistics."""
    
    def __init__(self, raw_text, words):
        """ This Initialize with raw text and 
             processed word list."""
        self.raw_text = raw_text
        self.words = words
        self.word_count = 0
        self.unique_words = 0
        self.chars_with_spaces = 0
        self.chars_no_spaces = 0
        self.avg_word_length = 0.0
        self.most_common_words = []
        self.most_common_count = 0
    
    def analyze(self):
        """This is to Calculate basic statistics
            like word count,unique words, and characterstats."""
            
        # Word count and unique words
        self.word_count = len(self.words)
        self.unique_words = len(set(self.words))
        
        # Count characters
        self.chars_with_spaces = len(self.raw_text)
        self.chars_no_spaces = len(self.raw_text.replace(" ", ""))

        # Average word length
        total_letters = 0
        for word in self.words:
            total_letters += len(word)
        if self.word_count > 0:
            self.avg_word_length = total_letters / self.word_count
        else:
            self.avg_word_length = 0.0
        
        # Find most common words
        if self.words:
            word_counts = Counter(self.words)
            max_count = max(word_counts.values())
            self.most_common_words = [word for word, count in word_counts.items() if count == max_count]
            self.most_common_words.sort()
            self.most_common_count = max_count
        else:
            self.most_common_words = []
            self.most_common_count = 0
        
        # Debug print for testing (can comment out)
        # print("Debug: analysis complete")

    def get_formatted_output(self):
        """It will return formatted text statistics as a string."""
        if self.most_common_words:
            common_words_str = ", ".join(self.most_common_words)
            common_display = f"{common_words_str} ({self.most_common_count})"
        else:
            common_display = "(0)"
        
        output_lines = [
            f"Word count: {self.word_count}",
            f"Unique words: {self.unique_words}",
            f"Characters (with spaces): {self.chars_with_spaces}",
            f"Characters (no spaces): {self.chars_no_spaces}",
            f"Average word length: {self.avg_word_length:.1f}",
            f"Most common word(s): {common_display}"
        ]
        return "\n".join(output_lines)
