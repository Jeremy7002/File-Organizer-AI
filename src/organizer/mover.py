import os
import shutil
from organizer.logger import log_action

def move_file(file_path, category, target_directory):
    """
    Moves a file to a folder named after its category inside target_directory.
    Handles duplicate file names by appending _1, _2, etc.
    Returns the final destination path.
    """

    # Full path of the category folder
    category_folder = os.path.join(target_directory, category)

    # Create folder if it doesn't exist
    os.makedirs(category_folder, exist_ok=True)

    # Get base file name and initial destination path
    base_name = os.path.basename(file_path)
    destination_path = os.path.join(category_folder, base_name)

    # Handle duplicate file names
    counter = 1
    name, ext = os.path.splitext(base_name)
    while os.path.exists(destination_path):
        new_name = f"{name}_{counter}{ext}"  # e.g., photo_1.jpg
        destination_path = os.path.join(category_folder, new_name)
        counter += 1
    try:
        shutil.move(file_path, destination_path)
    except Exception as e:
        print(f"Error moving file '{file_path}' to '{destination_path}': {e}")
        return file_path
    
    # Return final path (useful for logging)
    return destination_path