from features import extract_features
from scorer import calculate_score
from recommender import generate_recommendations

if __name__ == "__main__":
    with open("queries/sample.sql") as f:
        sql = f.read()
    features = extract_features(sql)
    score, drivers = calculate_score(features)
    recommendations = generate_recommendations(drivers)
    print(f"Score: {score}")
    print("Drivers: ")
    for d in drivers:
        print("-", d)
    print("Recommendations: ")
    for r in recommendations:
        print("-",r)
