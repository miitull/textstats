"""Text statistics helper functions (no file I/O)."""

import re
from collections import Counter

def count_characters_with_spaces(text):
    # Count all characters including spaces
    return len(text)

def count_characters_no_spaces(text):
    # Count characters excluding spaces
    count = 0
    for char in text:
        if not char.isspace():
            count += 1
    return count

def extract_words(text):
    # Extract only alphabetic words
    text = text.lower()
    return re.findall(r"[a-zA-Z]+", text)

def count_words(words):
    return len(words)

def count_unique_words(words):
    return len(set(words))

def calculate_average_word_length(words):
    if not words:
        return 0.0
    total = sum(len(w) for w in words)
    avg = total / len(words)
    return round(avg, 1)

def find_most_common_words(words):
    if not words:
        return [], 0
    counter = Counter(words)
    highest = max(counter.values())
    common_words = [w for w, c in counter.items() if c == highest]
    common_words.sort()
    return common_words, highest

def calculate_all_statistics(text):
    words = extract_words(text)
    most_common, freq = find_most_common_words(words)
    return {
        "word_count": count_words(words),
        "unique_words": count_unique_words(words),
        "chars_with_spaces": count_characters_with_spaces(text),
        "chars_no_spaces": count_characters_no_spaces(text),
        "avg_word_length": calculate_average_word_length(words),
        "most_common_words": most_common,
        "most_common_frequency": freq
    }

def format_output_lines(stats):
    if not stats["most_common_words"]:
        common_line = "Most common word(s): (0)"
    elif len(stats["most_common_words"]) == 1:
        common_line = f"Most common word(s): {stats['most_common_words'][0]} ({stats['most_common_frequency']})"
    else:
        common_line = f"Most common word(s): {', '.join(stats['most_common_words'])} ({stats['most_common_frequency']})"

    return [
        f"Word count: {stats['word_count']}",
        f"Unique words: {stats['unique_words']}",
        f"Characters (with spaces): {stats['chars_with_spaces']}",
        f"Characters (no spaces): {stats['chars_no_spaces']}",
        f"Average word length: {stats['avg_word_length']:.1f}",
        common_line
    ]
