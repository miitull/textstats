"""
File handling operations for text statistics program.
Handles user prompts, file reading, and file writing with error handling.
"""

import os

class FileHandler:
    """Manages all file input/output operations."""
    
def prompt_for_input_file(self):
    """Prompt user for input filename with validation."""
    while True:
        try:
            filename = input("Enter the input filename: ").strip()
            if not filename:
                print("Error: Input cannot be empty. Please try again.")
                continue
            
            # Check if file exists
            if not os.path.exists(filename):
                print(f"Error: File '{filename}' does not exist.")
                continue
            
            # Check if it's actually a file (not a directory)
            if not os.path.isfile(filename):
                print(f"Error: '{filename}' is not a file.")
                continue
                
            return filename
            
        except KeyboardInterrupt:
            print("\n\nProgram interrupted by user. Goodbye!")
            exit(0)
        except Exception as e:
            print(f"Unexpected error: {e}. Please try again.")
            
            
    
def prompt_for_output_file(self):
    """Prompt user for output filename with validation."""
    while True:
        try:
            filename = input("Enter output filename (default: output.txt): ").strip()
            if not filename:
                filename = "output.txt"

            # Check if file exists and ask for overwrite confirmation
            if os.path.exists(filename):
                response = input(f"File '{filename}' already exists. Overwrite? (y/n): ").strip().lower()
                if response not in ['y', 'yes']:
                    print("Operation cancelled. Please enter a different filename.")
                    continue

            return filename

        except KeyboardInterrupt:
            print("\nOperation cancelled.")
            return None
        except Exception as e:
            print(f"Error: {e}. Please try again.")
            
            
            
def read_file(self, filename):
    """Read and return contents of a file."""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read() 
            return content
    except FileNotFoundError:
        raise FileNotFoundError(f"Error: File '{filename}' not found.")
    except PermissionError:
        raise PermissionError(f"Error: Permission denied to read '{filename}'.")
    except UnicodeDecodeError:
        # Try with different encoding if UTF-8 fails
        try:
            with open(filename, 'r', encoding='latin-1') as file:
                return file.read()
        except UnicodeDecodeError:
            raise UnicodeDecodeError(f"Error: Cannot decode file '{filename}'.")
    except Exception as e:
        raise Exception(f"Error reading file '{filename}': {str(e)}")
    
    
    
def write_file(self, filename, content):
    """Write content to a file."""
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Results successfully written to '{filename}'")
    except PermissionError:
        raise PermissionError(f"Error: Permission denied to write to '{filename}'.")
    except Exception as e:
        raise Exception(f"Error writing to file '{filename}': {str(e)}")
    
    
    
