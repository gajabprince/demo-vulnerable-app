def login(username, password):
    query = "SELECT * FROM users WHERE name = %s"
    return db.execute(query, (username,))
