import cx_Oracle

def get_dba_tab_columns(USERNAME, SECRET, DSN, table):
    '''
    Gets the table columns detail.
    '''
    with cx_Oracle.connect(user=USERNAME, password=SECRET, dsn=DSN) as connection:
        with connection.cursor() as cursor:
            sql = f'''SELECT * FROM DBA_TAB_COLUMNS WHERE TABLE_NAME='{table}' '''
            cursor.execute(sql)
            rows = cursor.fetchall()
            columns = [col[0] for col in cursor.description]
            result = [dict(zip(columns, row)) for row in rows]
            return result

