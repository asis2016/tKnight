from .connector import database_connection

def get_database(host, user, secret, db):
    with database_connection(host, user, secret) as cursor:
        query = f"""SELECT
                    table_name,
                    Engine,
                    Version,
                    Row_format,
                    table_rows,
                    Avg_row_length,
                    Data_length,
                    Max_data_length,
                    Index_length,
                    Data_free,
                    Auto_increment,
                    DATE_FORMAT(Create_time, '%Y-%m-%d %H:%i:%s') AS Create_time,
                    DATE_FORMAT(Update_time, '%Y-%m-%d %H:%i:%s') AS Update_time,
                    DATE_FORMAT(Check_time, '%Y-%m-%d %H:%i:%s') AS Check_time,
                    table_collation,
                    Checksum,
                    Create_options,
                    table_comment
                    FROM
                        information_schema.tables
                    WHERE
                        table_schema = '{db}';"""
        
        cursor.execute(query)
        response = cursor.fetchall()

        result = [{
                    'table_name': table[0],
                    'engine': table[1],
                    'version': table[2],
                    'row_format': table[3],
                    'table_rows': table[4],
                    'avg_row_length': table[5],
                    'data_length': table[6],
                    'max_data_length': table[7],
                    'index_length': table[8],
                    'data_free': table[9],
                    'auto_increment': table[10],
                    'create_time': table[11],
                    'update_time': table[12],
                    'check_time': table[13],
                    'table_collation': table[14],
                    'checksum': table[15],
                    'create_options': table[16],
                    'table_comment': table[17]
                } 
                for table in response
            ]

    return {
        'result': result
    }
