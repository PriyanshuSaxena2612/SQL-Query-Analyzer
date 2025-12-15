Weights = {
    "join_count": 3,
    "cte_count": 3,
    "select_star": 10,
    "missing_where": 15,
    "windows_function": 8
}

def calculate_score(features):
    score = 0
    drivers = []
    
    score += features["join_count"] * Weights["join_count"]
    if features["join_count"] > 4:
        drivers.append(f"High JOIN count detected: {features['join_count']}")

    score += features["cte_count"] * Weights["cte_count"]
    if features["cte_count"] > 2:
        drivers.append(f"Multiple CTEs detected: {features['cte_count']}")

    if features["select_star"]:
        score += Weights["select_star"]
        drivers.append("SELECT * usage detected")

    if not features["has_where"]:
        score += Weights["missing_where"]
        drivers.append("Missing WHERE clause")

    score += features["windows_function"] * Weights['windows_function']
    if features["windows_function"]:
        drivers.append("Windows Function detected")

    return min(score, 100), drivers
        
