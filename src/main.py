import os
from organizer.scanner import scan_directory
from organizer.classifier import classify_file
from organizer.mover import move_file
from organizer.logger import log_action, log_new_run
import json

# Load configuration
def load_config(config_path="config/config.json"):
    """
    Loads configuration from JSON file.
    """
    with open(config_path, "r") as file:
        config = json.load(file)
    return config

def main():
    # Load config
    log_new_run()  # Log the start of a new run
    config = load_config()

    source_directory = config["source_directory"]
    destination_directory = config["destination_directory"]
    categories = config["categories"] # Not currently used, but can be for future enhancements
    
    # Scan for files
    files = scan_directory(source_directory)

    # Process each file
    for file_path in files:
        # Classify the file
        category = classify_file(file_path)

        # Move the file safely to the destination
        new_path = move_file(file_path, category, destination_directory)

        # Log the action
        log_action(file_path, category, new_path)

    print("\n File(s) successfully organized!")

if __name__ == "__main__":
    main()