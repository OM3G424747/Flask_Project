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

def check_data(data, column_name):
    connection = sqlite3.connect("flask_tut.db", check_same_thread = False)
    cursor = connection.cursor()
    cursor.execute(
        f"""
        SELECT {column_name}
        FROM users
        WHERE {column_name} = '{data}'
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

