import os

class FileRecord:
    def __init__(self, path):
        self.path = path
        self.name = os.path.basename(path)
        self.extension = os.path.splitext(path)[1].lower()

class ClassificationResult:
    def __init__(self, category, confidence):
        self.category = category
        self.confidence = confidence
