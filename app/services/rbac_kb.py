POLICY_STORE = [
    {"id": "kb_public", "min_role": 1, "topic": "workplace", "text": "Erha Technologies operates on a hybrid office model with flexible core collaboration hours."},
    {"id": "kb_eng", "min_role": 2, "topic": "engineering", "text": "Deployment keys and production secrets must be managed via HashiCorp Vault. Direct SSH is prohibited."},
    {"id": "kb_exec", "min_role": 3, "topic": "financial", "text": "Series A expansion reserves stand at $4.2M with allocation toward autonomous agent research."}
]

ROLE_LEVELS = {"intern": 1, "engineer": 2, "executive": 3}

def query_company_kb(query: str, user_role: str):
    role_lvl = ROLE_LEVELS.get(user_role.lower(), 1)
    q_low = query.lower()
    
    # Identify topic
    if "secret" in q_low or "production" in q_low or "ssh" in q_low:
        target = POLICY_STORE[1]
    elif "financial" in q_low or "reserve" in q_low or "series" in q_low:
        target = POLICY_STORE[2]
    else:
        target = POLICY_STORE[0]

    if role_lvl < target["min_role"]:
        return "ACCESS RESTRICTED: Your role permission level is insufficient to view this company policy.", False, None
    return target["text"], True, f"Policy Ref: #{target['id']} ({target['topic']})"
