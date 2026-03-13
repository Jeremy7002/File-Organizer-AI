import os
import shutil

def move_file(file_path, category, target_directory):
    """
    Moves a file to a folder named after its category inside target_directory.
    Handles duplicate file names by appending _1, _2, etc.
    Returns the final destination path.
    """

    # Full path of the category folder
    category_folder = os.path.join(target_directory, category)

    # Create folder if it doesn't exist
    if not os.path.exists(category_folder):
        os.makedirs(category_folder)

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

    # Move the file
    shutil.move(file_path, destination_path)

    # Return final path (useful for logging)
    return destination_path