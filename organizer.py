import os
import shutil

# Define categories and file extensions
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mov", ".avi"]
}

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

def create_folder(folder_name):
    folder_path = os.path.join(TARGET_FOLDER, folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    return folder_path

for item in os.listdir(TARGET_FOLDER):
    item_path = os.path.join(TARGET_FOLDER, item)

    # Only process files
    if os.path.isfile(item_path):
        file_ext = os.path.splitext(item)[1].lower()  # get file extension
        moved = False

        # Check each category
        for category, extensions in FILE_TYPES.items():
            if file_ext in extensions:
                dest_folder = create_folder(category)
                shutil.move(item_path, os.path.join(dest_folder, item))
                print(f"Moved {item} to {category}")
                moved = True
                break

        # If file doesn't match any category
        if not moved:
            dest_folder = create_folder("Others")
            shutil.move(item_path, os.path.join(dest_folder, item))
            print(f"Moved {item} to Others")
    else:
        print("Skipping folder:", item)
