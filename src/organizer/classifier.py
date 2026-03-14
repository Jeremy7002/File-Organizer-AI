import os
import json

def classify_file(file_path):
    """
    Determines the category of a file based on its extension.
    """

    # Extract file extension
    _, extension = os.path.splitext(file_path)

    extension = extension.lower()
    # Load categories from config
    with open("config/config.json", "r") as file:
        config = json.load(file)
        categories = config["categories"]

    # Classification rules
    for category, ext_list in categories.items():
        if extension in ext_list:
            return category

    return "Others"