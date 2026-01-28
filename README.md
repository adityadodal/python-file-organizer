# Python File Organizer

## Overview
Python File Organizer is an automation script that organizes files in a target directory
(such as Downloads) into folders based on file type.

It helps reduce clutter and demonstrates practical Python automation using file system operations.

---

## Problem Statement
Folders like Downloads often become messy with mixed file types.
Manually organizing them is repetitive and time-consuming.

This script automates the process by categorizing files into folders such as:
- Images
- Documents
- Videos
- Others

---

## Features
- Automatically scans a target directory
- Organizes files based on file extensions
- Creates folders dynamically if they don’t exist
- Safely moves files using Python standard libraries
- Ignores directories to avoid errors
- Easy to extend with new file categories

---

## Project Structure
python-file-organizer/
│
├── organizer.py
└── README.md


---

## How It Works
1. Reads all files from the target folder
2. Identifies file extensions
3. Matches extensions with predefined categories
4. Creates destination folders if required
5. Moves files into respective folders

---

## How to Run

1. Clone the repository:
```bash
git clone https://github.com/adityadodal/python-file-organizer.git

2. Navigate to the project folder:
cd python-file-organizer

3. Run the script:
python3 organizer.py

⚠️ macOS may require folder access permissions for Downloads.

Technologies Used

Python 3

os module

shutil module

Git & GitHub

What I Learned

Interacting with the operating system using Python

Automating repetitive tasks

File and directory handling

Writing clean and readable Python scripts

Using Git and GitHub for version control

Future Improvements

Command-line arguments for custom folders

Dry-run mode before moving files

Logging moved files

Error handling for edge cases

Author

Aditya Dodal
Python Developer | Automation & Cloud Enthusiast

