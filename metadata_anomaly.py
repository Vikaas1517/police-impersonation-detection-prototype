def compute_metadata_anomaly(account_age_days: int, total_posts: int) -> float:
    """
    Detects abnormal posting behavior.
    Returns anomaly score between 0 and 1.
    """
    if account_age_days <= 0:
        return 1.0

    posts_per_day = total_posts / account_age_days

    if posts_per_day > 10:
        return 1.0
    elif posts_per_day > 5:
        return 0.7
    elif posts_per_day > 2:
        return 0.4
    else:
        return 0.1
