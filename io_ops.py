
""" User interaction & file I/O."""

import os

def prompt_nonempty(prompt_text: str) -> str:
    """Prompt user for non-empty input with re-prompt on empty input."""
    while True:
        try:
            user_input = input(prompt_text).strip()
            if user_input:
                return user_input
            else:
                print("Error: Input cannot be empty. Please try again.")
        except KeyboardInterrupt:
            print("\n\nProgram interrupted by user. Goodbye!")
            exit(0)
        except Exception as e:
            print(f"Unexpected error: {e}. Please try again.")


def read_text_file(path: str) -> str:
    """Read text file with comprehensive error handling."""
    try:
        with open(path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"Error: File '{path}' not found.")
    except PermissionError:
        raise PermissionError(f"Error: Permission denied to read '{path}'.")
    except UnicodeDecodeError:
        # Try with different encoding if UTF-8 fails
        try:
            with open(path, 'r', encoding='latin-1') as file:
                return file.read()
        except UnicodeDecodeError:
            raise UnicodeDecodeError(f"Error: Cannot decode file '{path}' with common encodings.")
    except Exception as e:
        raise Exception(f"Error reading file '{path}': {str(e)}")


def confirm_overwrite(path: str) -> bool:
    """Ask user to confirm overwrite if file exists."""
    if not os.path.exists(path):
        return True
    
    while True:
        try:
            response = input(f"File '{path}' already exists. Overwrite? (y/n): ").strip().lower()
            if response in ['y', 'yes']:
                return True
            elif response in ['n', 'no']:
                return False
            else:
                print("Please enter 'y' for yes or 'n' for no.")
        except KeyboardInterrupt:
            print("\nOperation cancelled.")
            return False
        except Exception as e:
            print(f"Error: {e}. Please try again.")


def write_lines(path: str, lines: list) -> bool:
    """Write lines to file with error handling."""
    try:
        with open(path, 'w', encoding='utf-8') as file:
            for i, line in enumerate(lines):
                file.write(line)
                if i < len(lines) - 1:
                    file.write('\n')
        return True
    except PermissionError:
        raise PermissionError(f"Error: Permission denied to write to '{path}'.")
    except Exception as e:
        raise Exception(f"Error writing to file '{path}': {str(e)}")


def get_input_filename() -> str:
    """Getting valid input filename from user with validation."""
    while True:
        filename = prompt_nonempty("Enter the input filename: ")
        try:
            # Validate file exists and is readable
            if not os.path.exists(filename):
                print(f"Error: File '{filename}' does not exist.")
                continue
            if not os.path.isfile(filename):
                print(f"Error: '{filename}' is not a file.")
                continue
            return filename
        except Exception as e:
            print(f"Error: {e}")


def get_output_filename() -> str:
    """ To Get output filename from user with overwrite confirmation."""
    while True:
        output_file = input("Enter output filename (default: output.txt): ").strip()
        if not output_file:
            output_file = "output.txt"
        
        if not confirm_overwrite(output_file):
            continue  # User doesn't want to overwrite, re-prompt for filename
        
        return output_file


def prompt_save_results() -> str:
    """Asking user if they want to save results and get output filename."""
    while True:
        try:
            save = input("Save results to file? (y/n): ").strip().lower()
            if save in ['y', 'yes']:
                return get_output_filename()
            elif save in ['n', 'no']:
                return None
            else:
                print("Please enter 'y' for yes or 'n' for no.")
        except KeyboardInterrupt:
            print("\nOperation cancelled.")
            return None
        except Exception as e:
            print(f"Error: {e}. Please try again.")