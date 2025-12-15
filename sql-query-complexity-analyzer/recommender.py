def generate_recommendations(drivers):
    recs = []
    for d in drivers:
        if "JOIN" in d:
            recs.append("Review JOIN strategy or pre-aggregate data.")
        if "CTE" in d:
            recs.append("Reduce CTE depth or materialize intermediate results.")
        if "SELECT *" in d:
            recs.append("Replace SELECT * with explicity columns.")
        if "WHERE" in d:
            recs.append("Apply filters early to reduce scanned data.")
        if "Window" in d:
            recs.append("Evaluate window function cost.")

    return list(set(recs))
