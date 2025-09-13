# frequency.py

import sys
import re
from collections import Counter

def word_frequency(input_file: str, output_file: str):
    """
    Reads a text file, counts the frequency of words, and writes results to output file.
    Words are case-insensitive and punctuation is ignored.
    """
    try:
        # Read input file
        with open(input_file, "r", encoding="utf-8") as f:
            text = f.read()

        # Normalize text: lowercase and extract words only
        words = re.findall(r"\b\w+\b", text.lower())

        # Count word frequencies
        counter = Counter(words)

        # Sort by frequency (highest first), then alphabetically
        sorted_counts = sorted(counter.items(), key=lambda x: (-x[1], x[0]))

        # Write to output file
        with open(output_file, "w", encoding="utf-8") as f:
            for word, count in sorted_counts:
                f.write(f"{word} → {count}\n")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python frequency.py <input_file> <output_file>")
    else:
        word_frequency(sys.argv[1], sys.argv[2])
