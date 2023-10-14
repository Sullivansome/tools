import os
import re

def rename_files_in_directory(directory_path):
    # List all files in the specified directory
    files = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]

    for file_name in files:
        # Remove all contents in the "()" and () itself
        new_name = re.sub(r'\(.*?\)', '', file_name)

        # Replace "-" with " "
        new_name = re.sub(r'-', ' ', new_name)

        # Replace "_" with " "
        new_name = re.sub(r'_', ' ', new_name)

        # Remove "Z-Library"
        new_name = re.sub(r'Z-Library', '', new_name)

        # Change the file extension from .epub.pkgf to .epub
        new_name = re.sub(r'\.epub\.pkgf$', '.epub', new_name)

        # Ensure only one space between words
        new_name = re.sub(r'\s+', ' ', new_name)

        # Remove spaces after the last word but before the file extension
        new_name = re.sub(r'\s+(\.\w+)$', r'\1', new_name)

        # Rename the file if its name has changed
        if file_name != new_name:
            os.rename(os.path.join(directory_path, file_name), os.path.join(directory_path, new_name.strip()))

if __name__ == "__main__":
    directory = input("Enter the directory path: ")
    if os.path.exists(directory):
        rename_files_in_directory(directory)
        print("Files renamed successfully!")
    else:
        print("Directory not found.")
