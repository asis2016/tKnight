from .connector import database_connection

def get_schemas(host, username, secret):
    with database_connection(host, username, secret) as cursor:
        cursor.execute("SHOW SCHEMAS;")
        response = cursor.fetchall()

    result = [{'name': schema[0]} for schema in response]
    return {
        'result':result
    }

if __name__ == "__main__":
    get_schemas()
