from rapidfuzz import fuzz

def compute_name_similarity(name1: str, name2: str) -> float:
    """
    Returns similarity score between 0 and 1
    """
    if not name1 or not name2:
        return 0.0
    return fuzz.token_sort_ratio(name1, name2) / 100.0
