import json
import psycopg2
from datetime import date

class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, date):
            return obj.isoformat()
        return super().default(obj)

def fetch_table_data(cursor, table_name):
    query = f"SELECT * FROM {table_name};"
    cursor.execute(query)
    columns = [desc[0] for desc in cursor.description]
    rows = cursor.fetchall()

    table_data = []
    for row in rows:
        table_data.append(dict(zip(columns, row)))

    return table_data

def main():
    username = 'postgres'
    password = '12345'
    database = 'LAB3'
    host = 'localhost'
    port = '5432'

    connection_params = {
        "user": username,
        "password": password,
        "dbname": database,
        "host": host,
        "port": port
    }

    json_filename = 'exported_data.json'

    with psycopg2.connect(**connection_params) as conn, conn.cursor() as cursor:
        tables = ["director", "film", "genre"]

        data = {}
        for table in tables:
            table_data = fetch_table_data(cursor, table)
            data[table] = table_data

        with open(json_filename, 'w') as json_file:
            json.dump(data, json_file, indent=2, cls=DateEncoder)

if __name__ == "__main__":
    main()