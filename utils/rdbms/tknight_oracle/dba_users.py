import cx_Oracle

def get_dba_users(USERNAME, SECRET, DSN):
    '''
    `DBA_USERS` retrieves information about all users in the database. 
    '''
    with cx_Oracle.connect(user=USERNAME, password=SECRET, dsn=DSN) as connection:
        with connection.cursor() as cursor:
            sql = f'''SELECT * FROM DBA_USERS'''
            cursor.execute(sql)
            rows = cursor.fetchall()
            columns = [col[0] for col in cursor.description]
            result = [dict(zip(columns, row)) for row in rows]
            return result

