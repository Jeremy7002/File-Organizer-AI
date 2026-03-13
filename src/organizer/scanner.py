import os


def scan_directory(source_directory):
    """
    Scans the source directory and returns a list of file paths.
    """

    files = []

    for item in os.listdir(source_directory):
        full_path = os.path.join(source_directory, item)

        if os.path.isfile(full_path):
            files.append(full_path)

    return files