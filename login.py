def login(username, password):
    query = "SELECT * FROM users WHERE name='" + username + "'"
    return db.execute(query)
