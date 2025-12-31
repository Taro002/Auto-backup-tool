# Auto Backup Tool

A simple and automated Python tool to backup a folder, compress it, and optionally move it to a cloud sync folder.

## Features

- Backup entire folder
- Compress backup into a ZIP file
- Optional cloud sync folder support
- Logging of backup activity and errors

## Requirements

- Python 3.6+
- No external libraries required

## Configuration

1. Open `backup.py`.
2. Set the following variables:
   ```python
   SOURCE_DIR = r"PATH_TO_SOURCE_FOLDER"      # Folder to backup
   BACKUP_DIR = r"PATH_TO_BACKUP_FOLDER"      # Where backups are stored
   CLOUD_DIR = r"PATH_TO_CLOUD_FOLDER"       # Optional cloud sync folder (leave "" if not used)

## 📄 License

Copyright © 2025 Taro

Free for personal and educational use.

You are free to modify, improve, and redistribute this project.

---
