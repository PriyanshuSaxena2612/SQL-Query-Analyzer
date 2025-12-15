def extract_features(sql_text):
    sql_lower = sql_text.lower()
    return{
        "join_count": sql_lower.count(" join "),
        "cte_count": sql_lower.count(" with "),
        "select_star": int("select *" in sql_lower),
        "has_where": int(" where " in sql_lower),
        "windows_function": sql_lower.count(" over ")
    }
