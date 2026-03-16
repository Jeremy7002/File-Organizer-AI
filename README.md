# File Organizer AI System

## This project automatically organizes files into folders based on rules and later AI classification.

## Stage 1: Rule-based file organization

## Overview

Stage 1 implements a **rule-based file organizer** that automatically sorts files into categorized folders based on their file extensions.

The system scans a source directory, classifies each file using predefined rules from a configuration file, and moves them into appropriate category folders.

This stage establishes the **core automation pipeline** that later stages will enhance using machine learning and AI-based file understanding.

---

## Features

* Scans a directory for files
* Classifies files based on extension
* Automatically creates category folders if they do not exist
* Moves files into appropriate folders
* Maintains a log of all file operations
* Configuration-driven (no code modification needed to change categories)

---

## How It Works

1. **Scan Directory**

   * The program scans the source directory for files.

2. **Classify Files**

   * Each file extension is checked against rules defined in `rules.json`.

3. **Create Category Folder**

   * If the destination folder for that category does not exist, it is created.

4. **Move File**

   * The file is moved to the corresponding category folder.

5. **Log the Operation**

   * Each file movement is recorded in `logs/organizer.log`.

---

## Configuration

All settings are controlled using `config/rules.json`.

Example:

```json
{
  "source_directory": "tests/test_files",
  "destination_directory": "tests/organized_files",

  "categories": {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx"],
    "Music": [".mp3", ".wav", ".flac", ".aac"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".webm"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz", ".iso"],
    "Code": [".py", ".js", ".html", ".css", ".cpp", ".java"]
  }
}
```

Users can modify this file to customize how files are organized.

---

## Running the Program

Clone the repository:

```
git clone <repository-url>
cd file-organizer-ai
```

Run the program:

```
python main.py
```

---

## Logging

All file movements are logged in:

```
logs/organizer.log
```

Example log entry:

```
[2026-03-16 18:05:22] Moved 'photo.jpg' -> 'Images/photo.jpg' (Category: Images)
```

---

## Limitations of Stage 1

* Classification is based only on **file extensions**
* Cannot understand file content
* No machine learning yet

---


#### In Future
#### Stage 2: Machine learning classification
#### Stage 3: LLM file understanding
#### Stage 4: Autonomous file management agents

## Author

Jeremy James
