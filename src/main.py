import os
from organizer.scanner import scan_directory
from organizer.classifier import RuleBasedClassifier
from organizer.mover import move_file
from organizer.logger import log_action, log_new_run
from organizer.models import FileRecord
from organizer.decisions import should_move
import json

# Load configuration
def load_config(config_path="config/rules.json"):
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
    categories = config["categories"] 
    
    # Scan for files
    files = scan_directory(source_directory)
    dry_run = config.get("dry_run", False)
    classifier = RuleBasedClassifier(categories)
    # Process each file
    for file_path in files:
        # Classify the file
        record= FileRecord(file_path)
        result = classifier.classify(record)
        category = result.category

        # Decide whether to move the file
        if should_move(result):
            if dry_run:
                simulated_path = os.path.join(destination_directory, category, os.path.basename(file_path))
                log_action(file_path, category, simulated_path, "DRY_RUN")
            else:
                new_path = move_file(file_path, category, destination_directory)
                log_action(file_path, category, new_path, "MOVED")
        else:
            log_action(file_path, category, file_path, "SKIPPED")

    print("\n File(s) successfully organized!")

if __name__ == "__main__":
    main()