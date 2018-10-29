from tkinter import *
from tkinter import messagebox

import re

from bookstore_gui import BookWindow
from db_utils import db_connect, view_all_books, search_by_isbn, search_books, insert_book, update_book, delete_book, db_close  

__root__ = None
__window__ = None

def populate_listbox(books):
    max_width = [0,0,0,0]

    for book in books:
        for index, item in enumerate(book):
            length = len(str(item))
            if length > max_width[index]:
                max_width[index] = length

    box_length = 80
    isbn_length = max_width[0]
    author_length = max_width[2] if max_width[2] < 20 else 20
    year_length = 4
    title_length = box_length - isbn_length - author_length - year_length - 7 # 7 is for a space between each and quotes around title

    __window__.book_listbox.delete(0, __window__.book_listbox.size())
    for index, book in enumerate(books, 1):
        (isbn, title, author, year) = book

        title = title.strip()
        title = title if len(title) < title_length else (title[:(title_length - 3)] + '...') 
        title = "'" + title + "'"

        __window__.book_listbox.insert(index, f"{isbn:{isbn_length}} {title:{title_length}} {author:{author_length}} ({year:{year_length}})")

def command_view_all():
    __window__.book_isbn_entry_string.set("")
    __window__.book_title_entry_string.set("")
    __window__.book_author_entry_string.set("")
    __window__.book_year_entry_string.set("")

    books = view_all_books()
    populate_listbox(books)

def command_search():
    isbn = __window__.book_isbn_entry_string.get()
    title = __window__.book_title_entry_string.get()
    author = __window__.book_author_entry_string.get()
    year = __window__.book_year_entry_string.get()

    matching_books = search_books(isbn, title, author, year)
    populate_listbox(matching_books)

def command_insert():
    try:
        new_isbn = int(__window__.book_isbn_entry_string.get())
    except:
        return
    
    try:
        new_year = int(__window__.book_year_entry_string.get())
    except:
        return

    new_title = __window__.book_title_entry_string.get()
    new_author = __window__.book_author_entry_string.get()

    insert_book(new_isbn, new_title, new_author, new_year)
    command_view_all()

def command_update():
    pass

def command_delete():
    delete_book(get_isbn_from_current_selection())
    command_view_all()

def command_close():
    __root__.destroy()

def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        __root__.destroy()

def on_book_select(self):
    current_isbn = get_isbn_from_current_selection()
    current_book = search_by_isbn(current_isbn)
    (isbn, title, author, year) = current_book

    __window__.book_isbn_entry_string.set(isbn)
    __window__.book_title_entry_string.set(title)
    __window__.book_author_entry_string.set(author)
    __window__.book_year_entry_string.set(year)


def get_isbn_from_current_selection():
    booklist = __window__.book_listbox
    current = booklist.get(booklist.curselection())
    current_isbn = re.match(r"^\s*([0-9]+)\s+.*$", current).group(1)
    return current_isbn

def main():
    global __root__
    global __window__

    db_connect()

    __root__ = Tk()
    __root__.title("BookStore")
    __root__.resizable(width=False, height=False)    
    
    __window__ = BookWindow(__root__)

    __window__.book_listbox.bind('<<ListboxSelect>>', on_book_select)

    BookWindow.bind_command(__window__.button_view_command, command_view_all)
    BookWindow.bind_command(__window__.button_add_entry_command, command_insert)
    BookWindow.bind_command(__window__.button_search_command,command_search)
    BookWindow.bind_command(__window__.button_delete_command,command_delete)
    BookWindow.bind_command(__window__.button_close_command,command_close)

    command_view_all()

    __root__.protocol("WM_DELETE_WINDOW", on_closing)
    __root__.mainloop()
 
if __name__ == '__main__':
    main()