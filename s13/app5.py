import os
import sqlite3
from gui import BookWindow

DEFAULT_PATH = os.path.join(os.path.dirname(__file__), 'database.sqlite3')

def db_connect(db_path=DEFAULT_PATH):
    return sqlite3.connect(db_path)

def main():
    # TODO: Find out how to bind buttons to functions after declaration
    pass
 
if __name__ == '__main__':
    main()