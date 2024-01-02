import re

def extract_filename(file_path):
    match = re.search(r'[^\\/:*?"<>|\r\n]+$', file_path)
    return match.group() if match else None

# Test the function
file_path = "/path/to/file.txt"
print(extract_filename(file_path))  # Outputs: file.txt