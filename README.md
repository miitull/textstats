README

Project Overview:
This part of the assignment focused on Object-Oriented Programming. It continues from the earlier version where we used functions and now the program is refactored into classes and separate modules. So the goal is to make the code cleaner and more modular using OOP concepts.


Status Checklist:
- File handling module created
- Text processing module completed
- Text analysis module implemented
- Classes added for each module
- Docstrings added for all files, classes, and methods
- README and documentation updated


Class Design:
FileHandler
This class handles reading and writing text files. It checks if the file exists and handles file errors using exceptions.


TextProcessor
This class is responsible for cleaning and processing the text. It counts characters, words, and sentences and prepares the data for analysis.


TextAnalyzer
This class performs the main text analysis. It calculates statistics like word frequency, most common words, and overall summary.


How to Run:
1. Open the project folder in VS Code.
2. Make sure all the modules are in the same directory.
3. Run the main.py file.
4. The program will ask for a text file path, then show the calculated text statistics.


Command to run:
python main.py


Design Decisions:
It is divided into three modules:
file_handler.py handles all file operations.
text_processor.py does the text cleaning and processing.
text_analyzer.py does the statistical analysis.

This structure makes the project more organized and easier to maintain. It also helps in testing individual parts without affecting others.


Notes:
Tested everything in VS Code before committing to my branch in GitHub and also pasted the link below for my repoitory.


Repository:
GitHub: https://github.com/miitull/textstats


Branches:
main: Working OOP implementation

oop-refactor: Development history
