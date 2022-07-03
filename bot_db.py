import sqlite3


def db_input (effective_user, chat_id):
    connect = sqlite3.connect('db/bot_database.db')
    cursor = connect.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS bot_database(
        user_id      INTEGER NOT NULL,
        chat_id      INTEGER NOT NULL,
        user_name    TEXT,
        user_surname TEXT,
        username     STRING
    )""")
    connect.commit()
    people_id = effective_user.id
    cursor.execute(f"SELECT user_id FROM bot_database WHERE user_id = {people_id}")
    data_user = cursor.fetchone()
    if data_user is None:
        user_data = [effective_user.id, chat_id, effective_user.first_name, effective_user.last_name, effective_user.username]
        cursor.execute("INSERT INTO bot_database VALUES(?, ?, ?, ?, ?);", user_data)
        connect.commit()