import shutil
import os
from datetime import datetime
import logging

# ---------------- CONFIG ----------------
SOURCE_DIR = r"PATH_TO_SOURCE_FOLDER"      # Folder to backup
BACKUP_DIR = r"PATH_TO_BACKUP_FOLDER"      # Where backups are stored
CLOUD_DIR = r"PATH_TO_CLOUD_FOLDER"       # Optional cloud sync folder (leave "" if not used)
# ----------------------------------------

# Create backup directories if they don't exist
os.makedirs(BACKUP_DIR, exist_ok=True)
if CLOUD_DIR:
    os.makedirs(CLOUD_DIR, exist_ok=True)

# Setup logging
log_file = os.path.join(BACKUP_DIR, "backup_log.txt")
logging.basicConfig(filename=log_file,
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

try:
    # Timestamp for backup
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_name = f"backup_{timestamp}"
    backup_path = os.path.join(BACKUP_DIR, backup_name)

    # Copy the folder
    shutil.copytree(SOURCE_DIR, backup_path)
    
    # Compress to ZIP
    zip_path = backup_path + ".zip"
    shutil.make_archive(backup_path, 'zip', backup_path)
    
    # Optional: move to cloud sync folder
    if CLOUD_DIR:
        cloud_zip_path = os.path.join(CLOUD_DIR, os.path.basename(zip_path))
        shutil.move(zip_path, cloud_zip_path)
        logging.info(f"Backup completed and moved to cloud folder: {cloud_zip_path}")
    else:
        logging.info(f"Backup completed: {zip_path}")
    
    # Remove uncompressed backup folder
    shutil.rmtree(backup_path)

except Exception as e:
    logging.error(f"Backup failed: {e}")
