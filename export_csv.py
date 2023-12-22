import csv
import psycopg2

def export_table_to_csv(table_name, cursor):
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()

    csv_file_path = f"{table_name}.csv"

    with open(csv_file_path, 'w', encoding='utf-8', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([desc[0] for desc in cursor.description])
        csv_writer.writerows(rows)

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

    with psycopg2.connect(**connection_params) as conn, conn.cursor() as cursor:
        tables = ["director", "film", "genre"]

        for table in tables:
            export_table_to_csv(table, cursor)

if __name__ == "__main__":
    main()