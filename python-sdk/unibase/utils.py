def dict_to_conditions(where_dict: dict) -> list:
    """
    Converts a dictionary of key-value pairs into a list of condition dictionaries
    for the Unibase API.
    Example: {"role": "admin"} -> [{"field": "role", "operator": "=", "value": "admin"}]
    """
    if not where_dict:
        return []
    conditions = []
    for k, v in where_dict.items():
        conditions.append({
            "field": k,
            "operator": "=",
            "value": v
        })
    return conditions
