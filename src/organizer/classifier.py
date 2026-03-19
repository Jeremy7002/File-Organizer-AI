from organizer.models import ClassificationResult

class RuleBasedClassifier:
    def __init__(self, categories):
        self.categories = categories

    def classify(self, file_record):
        for category, ext_list in self.categories.items():
            if file_record.extension in ext_list:
                return ClassificationResult(category, 1.0)

        return ClassificationResult("Others", 0.5)