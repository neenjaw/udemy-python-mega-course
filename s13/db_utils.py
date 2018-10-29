import os
import sqlite3

DEFAULT_PATH = os.path.join(os.path.dirname(__file__), 'database.sqlite3')

__DB__ = None

class DbException(Exception):
    pass

"""
db_connect()
"""
def db_connect(db_path=DEFAULT_PATH):
    global __DB__
    if __DB__ is not None: return

    __DB__ = sqlite3.connect(db_path)
    create_bookstore_table()

def is_db_connection_open():
    if __DB__ is None:
        return False
    else:
        return True

"""
db_close()
"""
def db_close():
    global __DB__   
    if not is_db_connection_open():
        raise DbException

    __DB__.close()

"""
create_bookstore_table()
"""
def create_bookstore_table():
    global __DB__    
    if not is_db_connection_open():
        raise DbException

    create_sql = """
        CREATE TABLE IF NOT EXISTS bookstore (
                isbn INTEGER PRIMARY KEY,
                title STRING NOT NULL,
                author STRING NOT NULL,
                year INTEGER NOT NULL
        )
        """

    c = __DB__.cursor()
    c.execute(create_sql)
    
    __DB__.commit()

"""
view_all_books()
"""
def view_all_books():
    global __DB__    
    if not is_db_connection_open():
        raise DbException

    view_sql = """
        SELECT * FROM bookstore
        """

    c = __DB__.cursor()
    c.execute(view_sql)

    return c.fetchall()

"""
search_by_isbn()
"""
def search_by_isbn(isbn):
    global __DB__    
    if not is_db_connection_open():
        raise DbException

    search_sql = """
        SELECT 
            * 
        FROM 
            bookstore b
        WHERE 
            b.isbn = ?
    """

    c = __DB__.cursor()
    c.execute(search_sql, (isbn,))
    
    return c.fetchone()

"""
search_books()
"""
def search_books(isbn="", title="", author="", year=""):
    global __DB__    
    if not is_db_connection_open():
        raise DbException

    search_sql = """
        SELECT 
            * 
        FROM 
            bookstore b
        WHERE 
            b.isbn = ?
        OR
            b.title = ?
        OR
            b.author = ?
        OR
            b.year = ?
    """

    c = __DB__.cursor()
    c.execute(search_sql, (isbn, title, author, year,))
    
    return c.fetchall()
    
"""
insert_book()
"""
def insert_book(isbn, title, author, year):
    global __DB__    
    if not is_db_connection_open():
        raise DbException

    insert_sql = """
        INSERT INTO bookstore (isbn, title, author, year) VALUES (?,?,?,?) 
    """

    c = __DB__.cursor()
    c.execute(insert_sql, (isbn, title, author, year,))

    __DB__.commit()
    
"""
update_book()
"""
def update_book(isbn, new_isbn, new_title, new_author, new_year):
    global __DB__    
    if not is_db_connection_open():
        raise DbException

    update_sql = """
        UPDATE bookstore SET isbn=?, title=?, author=?, year=? WHERE isbn=?
    """
    
    c = __DB__.cursor()
    c.execute(update_sql, (new_isbn, new_title, new_author, new_year, isbn, ))

    __DB__.commit()

"""
delete_book()
"""
def delete_book(isbn):
    global __DB__    
    if not is_db_connection_open():
        raise DbException

    delete_sql = """
        DELETE FROM bookstore WHERE isbn=?
    """

    c = __DB__.cursor()
    c.execute(delete_sql, (isbn,))
    __DB__.commit()

def main():
    db_connect()

    # insert_book(123412341234, "How to Kill a Mockingbird", "Unknown", 1963)

    print(view_all_books())

    db_close()

if __name__ == '__main__':
    main()