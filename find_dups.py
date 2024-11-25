import os
from collections import defaultdict

def find_duplicate_filenames(directory):
    file_names = defaultdict(list)

    for root, _, files in os.walk(directory):
        for file in files:
            file_names[file].append(os.path.join(root, file))

    duplicates = {name: paths for name, paths in file_names.items() if len(paths) > 1}

    return duplicates

# Example usage
directory = "C:/Users/abrow/OneDrive/Pictures/pictures"
duplicates = find_duplicate_filenames(directory)

if duplicates:
    for name, paths in duplicates.items():
        print(f"Duplicate file: {name}")
        for path in paths:
            print(f" - {path}")
else:
    print("No duplicate files found.")
