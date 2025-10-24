"""Entry point for the Text Statistics Analyzer program."""

from io_ops import get_input_filename, read_text_file, prompt_save_results, write_lines
from text_stats import calculate_all_statistics, format_output_lines


def main() -> None:
    """Main program orchestration."""
    print("=== Text Statistics Analyzer ===\n")
    
    # Getting input path (prompt)
    input_filename = get_input_filename()
    
    try:
        # Read text (io_ops)
        print(f"Reading file: {input_filename}")
        text_content = read_text_file(input_filename)
        
        # Compute metrics (text_stats)
        print("Analyzing text...")
        stats = calculate_all_statistics(text_content)
        output_lines = format_output_lines(stats)
        
        # Print to console
        print("\n=== Analysis Results ===")
        for line in output_lines:
            print(line)
        
        # Write to output file (io_ops)
        output_filename = prompt_save_results()
        if output_filename:
            try:
                write_lines(output_filename, output_lines)
                print(f"Results successfully saved to: {output_filename}")
            except Exception as e:
                print(f"Warning: {e}")
        else:
            print("Results not saved to file.")
            
    except Exception as e:
        print(f"Error: {e}")
        return
    
    print("\nAnalysis complete!")


if __name__ == "__main__":
    main()
