import os
import shutil

# Define the paths for the source, search, and destination folders
source_folder = r"C:\Users\Neil Buffham\Pictures\mtsa"
search_folder = r"C:\memes\crop-source"
destination_folder = r"C:\memes\new-source"

# Get the list of file names from the source folder
file_names = os.listdir(source_folder)

# Ensure the destination folder exists
os.makedirs(destination_folder, exist_ok=True)

# Search for matching files in the search folder and copy them to the destination folder
for file_name in file_names:
    search_path = os.path.join(search_folder, file_name)
    if os.path.exists(search_path):
        shutil.copy2(search_path, destination_folder)
        print(f"Copied: {file_name}")
    else:
        print(f"Not found: {file_name}")

print("Operation completed.")
