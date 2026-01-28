import os
import shutil

TARGET_FOLDER = os.path.expanduser("~/Downloads")

print("Organizing files in:", TARGET_FOLDER)

# List all items in folder
for item in os.listdir(TARGET_FOLDER):
    item_path = os.path.join(TARGET_FOLDER, item)

    # Only process files (ignore folders)
    if os.path.isfile(item_path):
        print("File:", item)
    else:
        print("Skipping folder:", item)
