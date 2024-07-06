import os

# Create a dictionary to store file names and their corresponding paths
file_dict = {}

# Traverse through all directories and files in 'K:/pictures'
for dp, dn, filenames in os.walk('K:/pictures'):
    for f in filenames:
        # Check if the file has a '.jpg' extension
        if os.path.splitext(f)[1].lower() == '.jpg':
            # Get the full path of the file
            file_path = os.path.join(dp, f)
            # Check if the file name already exists in the dictionary
            if f in file_dict:
                # If the file name already exists, append the new path to the existing list of paths
                file_dict[f].append(file_path)
            else:
                # If the file name doesn't exist in the dictionary, add it as a new key-value pair
                file_dict[f] = [file_path]

# Filter the dictionary to only include file names with multiple paths
duplicate_files = {k: v for k, v in file_dict.items() if len(v) > 1}

# Filter the duplicate files dictionary to only include files whose duplicates are also located in the specified directory
# camera_unorganized_duplicates = {k: v for k, v in duplicate_files.items() if all(os.path.dirname(path) == 'directory' for path in v)}
#
# # Create a list of duplicate file paths
# duplicate_paths = [path for paths in camera_unorganized_duplicates.values() for path in paths]
#
# # Print the list of duplicate file paths
# for file_path in duplicate_paths:
#     print(file_path)

# Print the list of duplicate file names and their paths
for file_name, file_paths in duplicate_files.items():
    print(f"{file_name}:")
    for file_path in file_paths:
        print(f"\t{file_path}")