import os


def classify_file(file_path):
    """
    Determines the category of a file based on its extension.
    """

    # Extract file extension
    _, extension = os.path.splitext(file_path)

    extension = extension.lower()

    # Classification rules
    if extension in [".jpg", ".jpeg", ".png", ".gif"]:
        return "Images"

    elif extension in [".pdf", ".doc", ".docx", ".txt"]:
        return "Documents"

    elif extension in [".mp4", ".mkv", ".avi"]:
        return "Videos"

    elif extension in [".mp3", ".wav"]:
        return "Audio"

    elif extension in [".py", ".java", ".c", ".cpp"]:
        return "Code"

    elif extension in [".zip", ".rar"]:
        return "Archives"
    
    else:
        return "Others"