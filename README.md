# Text Stats - Refactor Starter

## Overview
This project is a refactored version of a basic text stats program.  
The main goal was to separate the logic into three modules so the code is cleaner, easier to test, and doesn't crash on bad input.

- text_stats.py - handles all text calculations only (no input/output or try/except)
- io_ops.py - manages user input, file reading/writing, and error handling  
- main.py - connects both modules and runs the whole program

---

## How to Run

python main.py
When you run it, the program will:

Ask for an input filename

Show these results:

Word count

Unique words

Characters (with spaces)

Characters (without spaces)

Average word length (one decimal)

Most common word(s) - alphabetical order for ties, (0) if no words

Ask if you want to save results (default file is output.txt)

## Modules
text_stats.py - pure text processing, no file or user interaction
io_ops.py - handles prompts, reading/writing files, and try/except blocks
main.py - keeps things minimal and only calls functions

## Definition of Done
main.py only orchestrates

text_stats.py has no input/output or exception handling

io_ops.py safely handles all file operations and user input

Program never crashes - re-prompts or exits cleanly

Output matches the required format

README is updated with how to run and what was tested

# Testing
I tested the program with:

Normal text files

Empty files

Files that only had spaces

Nonexistent files

Invalid user input

Everything worked fine without crashing or breaking.

## My Work
I completed this project individually.
I wrote the text-processing functions, added file and input validation, handled errors safely, tested edge cases, and wrote this README.

Assignment-3 README

