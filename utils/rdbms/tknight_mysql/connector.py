import mysql.connector
from contextlib import contextmanager

@contextmanager
def database_connection(host, user, secret):
    db = mysql.connector.connect(
        host=host,
        user=user,
        password=secret
    )
    cursor = db.cursor()
    try:
        yield cursor
    finally:
        cursor.close()
        db.close()
