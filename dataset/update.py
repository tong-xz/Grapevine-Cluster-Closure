def replace_in_file(file_path, new_file_path=None):
    """
    Replace all backslashes (\) with forward slashes (/) in each line of the file.

    Args:
    - file_path (str): Path to the original file.
    - new_file_path (str, optional): Path to the output file. If not specified, the original file will be overwritten.

    Returns:
    None
    """
    # Initialize an empty list to hold the modified lines
    modified_lines = []

    # Open the original file and read line by line
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # Replace backslashes with forward slashes in the current line
            modified_line = line.replace('\\', '/')
            modified_lines.append(modified_line)
    
    # Write the modified lines to the new file or overwrite the original file
    output_path = new_file_path if new_file_path else file_path
    with open(output_path, 'w', encoding='utf-8') as file:
        file.writelines(modified_lines)

    print(f"File has been updated and saved to {output_path}")

# Example usage
# replace_in_file('path/to/your/original_file.txt', 'path/to/your/new_file.txt')
# If you want to overwrite the original file, you can call it like this:
# replace_in_file('path/to/your/original_file.txt')


# Example usage
# Replace the 'your_file_path_here' with the path to your file
# replace_backslashes('your_file_path_here')

file_path = 'dataset/train.txt'
new_path = 'dataset/train2.txt'
replace_in_file(file_path, new_path)