import os
import sqlite3

DEFAULT_PATH = os.path.join(os.path.dirname(__file__), 'database.sqlite3')

def get_db_conn(db_path=DEFAULT_PATH):
    return sqlite3.connect(db_path)

def close_db_conn(db_conn):
    db_conn.close()

def create_table(db_conn):
    cursor = db_conn.cursor()

    # cursor.execute("DROP TABLE IF EXISTS fruit;")

    create_table_sql = """
        CREATE TABLE IF NOT EXISTS fruit (
            item TEXT PRIMARY KEY,
            quantity INTEGER, 
            price REAL
        );
        """
    cursor.execute(create_table_sql)

    db_conn.commit()

def insert(db_conn, item, quantity, price):
    cursor = db_conn.cursor()

    # this is not safe, injection vulnerable
    # cursor.execute(f"INSERT INTO fruits (item, quantity, price) VALUES ({item}, {quantity}, {price})")

    cursor.execute("INSERT INTO fruit (item, quantity, price) VALUES (?,?,?)", (item, quantity, price))
    db_conn.commit()

def view_rows(db_conn):
    cursor = db_conn.cursor()

    view_sql = """
        SELECT * FROM fruit
        """
    cursor.execute(view_sql)
    rows = cursor.fetchall()
    return rows


conn = get_db_conn()
create_table(conn)
insert(conn, "coffee cup", 10, 5)

for row in view_rows(conn):
    print(row)

formatted_result = [f"{name:<20}{quantity:<6}{price:>5}" for name, quantity, price in view_rows(conn)]
name, quantity, price = "Name", "Qty", "Price"
print("\n".join([f"{name:<20}{quantity:<6}{price:>5}"] + formatted_result))

conn.close()