from src.database.database import Database
from sqlite3 import Error


def create_table(conn):
    try:
        conn.execute('''CREATE TABLE HISTORIQUE
                (INPUT TEXT    NOT NULL,
                RESULT INTEGER NOT NULL);''')
    except Error as e:
        print(e)


def intitialize_database():
    db = Database()
    conn = db.create_connection()
    create_table(conn)
    db.close_connexion()


if __name__ == '__main__':
    intitialize_database()
