from .connector import database_connection

def get_describe_table(host, username, secret, db, table):
    with database_connection(host, username, secret) as cursor:
        #DESCRIBE TABLE_NAME;
        query = f"""
                SELECT COLUMN_NAME, 
                DATA_TYPE, 
                CHARACTER_MAXIMUM_LENGTH,
                IS_NULLABLE, 
                COLUMN_DEFAULT
                FROM INFORMATION_SCHEMA.COLUMNS
                WHERE TABLE_SCHEMA = '{db}' AND TABLE_NAME = '{table}';        
                """

        cursor.execute(query)
        response = cursor.fetchall()

    result = [{
            'col_name': table[0],
            'data_type': table[1],
            'char_max_len': table[2],
            'is_nullable': table[3],
            'column_default': table[4]
        }
        for table in response
    ]

    return {
        'result': result
    }

if __name__ == '__main__':
    get_describe_table()
