def vulnerable_login(username):
    query = f"SELECT * FROM users WHERE username = '{username}'"
    return query