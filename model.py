import sqlite3

def show_word(username):
    connection = sqlite3.connect("flask_tut.db", check_same_thread = False)
    cursor = connection.cursor()
    cursor.execute(
        f"""
        SELECT secret_word
        FROM users
        WHERE username = '{username}';
        """
    )
    word = cursor.fetchone()[0]

    connection.commit()
    cursor.close()
    connection.close()

    message = f"{username}'s secret word is \"{word}\", don't tell anyone."
    return message


def check_pass(username):
    connection = sqlite3.connect("flask_tut.db", check_same_thread = False)
    cursor = connection.cursor()
    cursor.execute(
        f"""
        SELECT password
        FROM users
        WHERE username = '{username}';
        """
    )

    try:
        result = cursor.fetchone()[0]
    except:
        # returns negative 1 to indicate an error
        result = -1

    connection.commit()
    cursor.close()
    connection.close()

    return result


def check_users():
    connection = sqlite3.connect("flask_tut.db", check_same_thread = False)
    cursor = connection.cursor()
    cursor.execute(
        f"""
        SELECT username
        FROM users
        ORDER BY pk DESC;
        """
    )

    try:
        db_users = cursor.fetchall()
        result = []

        for i in range(len(db_users)):
            user = db_users[i][0]
            result.append(user)

    except:
        # returns negative 1 to indicate an error
        result = -1

    connection.commit()
    cursor.close()
    connection.close()

    return result


def signup(username, password, secret_word):
    connection = sqlite3.connect("flask_tut.db", check_same_thread = False)
    cursor = connection.cursor()
    cursor.execute(
        f"""
        SELECT username
        FROM users
        WHERE username = '{username}';
        """
    )
    
    try:
        result = cursor.fetchone()[0]
    except:
        # returns negative 1 to indicate an error
        result = -1

    if result == -1:
        cursor.execute(
        f"""
        INSERT INTO users(
        username,
        password,
        secret_word
        )
        VALUES(
        '{username}',
        '{password}',
        '{secret_word}'
        );
        """
        )
    else:
        connection.commit()
        cursor.close()
        connection.close()
        return "Username already in use."

    connection.commit()
    cursor.close()
    connection.close()
    return "User registered successfully."
