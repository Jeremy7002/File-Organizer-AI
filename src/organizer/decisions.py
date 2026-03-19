def should_move(result):
    """
    Decides whether a file should be moved based on classification confidence.
    """
    if result.category == "Others":
        return True  # Always move to 'Others' for manual review
    if result.confidence >= 0.8:
        return True
    return False