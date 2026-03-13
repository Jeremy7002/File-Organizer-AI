import json
import os


def load_config(config_path="config/config.json"):
    """
    Loads configuration from JSON file.
    """
    with open(config_path, "r") as file:
        config = json.load(file)
    return config


def main():
    # Load configuration
    config = load_config()

    source_directory = config["source_directory"]
    destination_directory = config["destination_directory"]
    categories = config["categories"]

    print("Source Directory:", source_directory)
    print("Destination Directory:", destination_directory)
    print("Categories:", categories)


if __name__ == "__main__":
    main()