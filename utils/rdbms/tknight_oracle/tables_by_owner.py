import cx_Oracle

def get_tables_by_owner(USERNAME, SECRET, DSN, owner):
    '''
    Get all tables owned by the `owner`.
    '''
    with cx_Oracle.connect(user=USERNAME, password=SECRET, dsn=DSN) as connection:
        with connection.cursor() as cursor:
            sql = f'''SELECT * FROM ALL_TABLES WHERE OWNER='{owner}' '''
            cursor.execute(sql)
            rows = cursor.fetchall()
            columns = [col[0] for col in cursor.description]
            result = [dict(zip(columns, row)) for row in rows]
            return result

