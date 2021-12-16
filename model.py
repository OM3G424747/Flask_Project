import sqlite3

def show_word(username):
    connection = sqlite3.connect("flask_tut.db", check_same_thread = False)
    cursor = connection.cursor()
    cursor.execute(
        f"""
        SELECT secret_word
        FROM users
        WHERE username = '{username}'
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
        WHERE username = '{username}'
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


def signup(username, password, secret_word):
    connection = sqlite3.connect("flask_tut.db", check_same_thread = False)
    cursor = connection.cursor()
    cursor.execute(
        f"""
        SELECT username
        FROM users
        WHERE username = '{username}'
        """
    )
    result = cursor.fetchone()[0]
    
    if result is None:
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


    connection.commit()
    cursor.close()
    connection.close()