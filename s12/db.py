import os
import sqlite3

DEFAULT_PATH = os.path.join(os.path.dirname(__file__), 'database.sqlite3')

def get_db_conn(db_path=DEFAULT_PATH):
    return sqlite3.connect(db_path)

def close_db_conn(db_conn):
    db_conn.close()

def create_table(db_conn):
    cursor = db_conn.cursor()

    cursor.execute("DROP TABLE IF EXISTS fruit;")

    create_table_sql = """
        CREATE TABLE IF NOT EXISTS fruit (
            name TEXT PRIMARY KEY,
            quantity INTEGER, 
            price REAL
        );
        """
    cursor.execute(create_table_sql)

    db_conn.commit()

def insert(db_conn, name, quantity, price):
    cursor = db_conn.cursor()

    # this is not safe, injection vulnerable
    # cursor.execute(f"INSERT INTO fruits (name, quantity, price) VALUES ({name}, {quantity}, {price})")

    cursor.execute("INSERT INTO fruit (name, quantity, price) VALUES (?,?,?)", (name, quantity, price))
    db_conn.commit()

def view(db_conn):
    cursor = db_conn.cursor()

    view_sql = """
        SELECT * FROM fruit
        """
    cursor.execute(view_sql)
    rows = cursor.fetchall()
    return rows
    
def view_formatted(db_conn):
    formatted_result = [f"{name:<20}{quantity:<6}{price:>5}" for name, quantity, price in view(db_conn)]
    name, quantity, price = "Name", "Qty", "Price"
    return "\n".join([f"{name:<20}{quantity:<6}{price:>5}"] + formatted_result)

def delete(db_conn, name):
    cursor = db_conn.cursor()

    delete_sql = """
        DELETE FROM fruit WHERE name=?
        """
    cursor.execute(delete_sql, (name,))
    db_conn.commit()

def update_price(db_conn, name, price):
    cursor = db_conn.cursor()

    update_sql = """
        UPDATE fruit SET price=? WHERE name=?
        """    
    cursor.execute(update_sql, (price, name))
    db_conn.commit()




conn = get_db_conn()

create_table(conn)

insert(conn, "coffee", 10, 5)

update_price(conn, "coffee", 8.56)

print(view_formatted(conn))

delete(conn, "coffee")

print(view_formatted(conn))

conn.close()