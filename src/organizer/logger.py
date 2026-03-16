import os
from datetime import datetime

# Optional: store logs in a 'logs' folder
LOG_FOLDER = "logs"

os.makedirs(LOG_FOLDER, exist_ok=True)

LOG_FILE = os.path.join(LOG_FOLDER, "organizer.log")

def log_new_run():
    with open("logs/organizer.log", "a", encoding="utf-8") as f:
        f.write("\n")  # Add a newline for separation
        f.write(f"--- New Run started at {datetime.now().strftime("%Y-%m-%d %H:%M:%S")} ---\n")

def log_action(original_path, category, new_path):
    """
    Appends a log entry with timestamp for a moved file.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{timestamp}] Moved '{original_path}' -> '{new_path}' (Category: {category})"

    # Append entry to log file
    with open(LOG_FILE, "a",encoding="utf-8") as f:
        f.write(entry+'\n')
