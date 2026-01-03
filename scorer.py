def compute_risk_score(features: dict) -> float:
    """
    Combines feature scores into a final risk score (0–100)
    """
    score = (
        0.35 * features["name_similarity"] +
        0.35 * features["image_similarity"] +
        0.30 * features["metadata_anomaly"]
    )

    return round(score * 100, 2)
