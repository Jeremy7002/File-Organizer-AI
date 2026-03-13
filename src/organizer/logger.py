import os
from datetime import datetime

# Optional: store logs in a 'logs' folder
LOG_FOLDER = "logs"
if not os.path.exists(LOG_FOLDER):
    os.makedirs(LOG_FOLDER)

LOG_FILE = os.path.join(LOG_FOLDER, "organizer.log")

def log_action(original_path, category, new_path):
    """
    Appends a log entry with timestamp for a moved file.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{timestamp}] Moved '{original_path}' → '{new_path}' (Category: {category})\n"

    # Append entry to log file
    with open(LOG_FILE, "a") as f:
        f.write(entry)