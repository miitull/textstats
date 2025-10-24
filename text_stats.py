"""
Pure text-processing functions (no I/O or exceptions).
"""

import re
from collections import Counter


def count_characters_with_spaces(text: str) -> int:
    """Count all characters including spaces."""
    return len(text)


def count_characters_no_spaces(text: str) -> int:
    """Count characters excluding spaces."""
    characters_no_spaces = 0
    for char in text:
        if not char.isspace():
            characters_no_spaces += 1
    return characters_no_spaces


def extract_words(text: str) -> list:
    """Extract words: letters only (A–Z/a–z), case-insensitive."""
    lowered_text = text.lower()
    return re.findall(r"[a-zA-Z]+", lowered_text)


def count_words(word_list: list) -> int:
    """Count total number of words."""
    return len(word_list)


def count_unique_words(word_list: list) -> int:
    """Count number of unique words."""
    return len(set(word_list))


def calculate_average_word_length(word_list: list) -> float:
    """Calculate average word length with one decimal precision."""
    if not word_list:
        return 0.0
    
    total_letter_count = sum(len(word) for word in word_list)
    return round(total_letter_count / len(word_list), 1)


def find_most_common_words(word_list: list) -> tuple:
    """
    Find the most common word(s) and their frequency.
    Returns tuple: (list of words, frequency)
    Returns ([], 0) if no words.
    """
    if not word_list:
        return ([], 0)
    
    word_counts = Counter(word_list)
    highest_frequency = max(word_counts.values())
    most_frequent_words = [word for word, count in word_counts.items() 
                          if count == highest_frequency]
    most_frequent_words.sort()
    
    return (most_frequent_words, highest_frequency)


def format_most_common_line(most_frequent_words: list, frequency: int) -> str:
    """Format the most common words line according to requirements."""
    if not most_frequent_words:
        return "Most common word(s): (0)"
    elif len(most_frequent_words) == 1:
        return f"Most common word(s): {most_frequent_words[0]} ({frequency})"
    else:
        return f"Most common word(s): {', '.join(most_frequent_words)} ({frequency})"


def calculate_all_statistics(text: str) -> dict:
    """Calculate all text statistics and return as dictionary."""
    words = extract_words(text)
    most_common_words, frequency = find_most_common_words(words)
    
    return {
        'word_count': count_words(words),
        'unique_words': count_unique_words(words),
        'chars_with_spaces': count_characters_with_spaces(text),
        'chars_no_spaces': count_characters_no_spaces(text),
        'avg_word_length': calculate_average_word_length(words),
        'most_common_words': most_common_words,
        'most_common_frequency': frequency
    }


def format_output_lines(stats: dict) -> list:
    """Format statistics into the six required output lines."""
    most_common_line = format_most_common_line(
        stats['most_common_words'], 
        stats['most_common_frequency']
    )
    
    return [
        f"Word count: {stats['word_count']}",
        f"Unique words: {stats['unique_words']}",
        f"Characters (with spaces): {stats['chars_with_spaces']}",
        f"Characters (no spaces): {stats['chars_no_spaces']}",
        f"Average word length: {stats['avg_word_length']:.1f}",
        most_common_line
    ]