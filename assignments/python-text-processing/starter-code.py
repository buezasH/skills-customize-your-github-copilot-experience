def analyze_text(filename):
    """Read a text file and display a summary of its contents."""
    # TODO: Read the contents of the file
    # TODO: Count the total number of lines, words, and characters
    # TODO: Find the 5 most frequently used words (case-insensitive)
    # TODO: Handle the case where the file does not exist
    pass


def transform_text(input_filename, output_filename):
    """Transform text and write the results to an output file."""
    # TODO: Read the input file
    # TODO: Convert all text to title case
    # TODO: Remove blank lines
    # TODO: Add line number prefixes in the format "001: "
    # TODO: Write the transformed text to the output file
    # TODO: Print a confirmation message and preview the first 3 lines
    pass


if __name__ == "__main__":
    print("=== Task 1: Analyze Text File ===")
    analyze_text("sample-text.txt")

    print("\n=== Task 2: Transform and Write Text ===")
    transform_text("sample-text.txt", "output.txt")
