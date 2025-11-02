"""
File handling operations for text statistics program.
Handles user prompts, file reading, and file writing with error handling.
"""

import os

class FileHandler:
    """Handles all file input and output operations."""
    
    def prompt_for_input_file(self):
        """Ask user for a valid input file path."""
        while True:
            file_name = input("Enter the input file name: ").strip()
            if os.path.exists(file_name):
                return file_name
            else:
                print("Error: File not found. Please try again.")

    def prompt_for_output_file(self):
        """Ask user for output file name to save results."""
        file_name = input("Enter output file name: ").strip()
        return file_name

    def read_file(self, filename):
        """Read and return contents of a file."""
        try:
            with open(filename, "r", encoding="utf-8") as f:
                return f.read()
        except FileNotFoundError:
            print("Error: File not found.")
            return ""
        except Exception as e:
            print("Error reading file:", e)
            return ""

    def write_file(self, filename, content):
        """Write text statistics to an output file."""
        try:
            with open(filename, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Results saved to {filename}")
        except Exception as e:
            print("Error writing file:", e)
