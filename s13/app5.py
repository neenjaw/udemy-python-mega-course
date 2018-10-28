from tkinter import *
from tkinter import messagebox

from bookstore_gui import BookWindow
from db_utils import db_connect, view_all_books, search_book, insert_book, update_book, delete_book, db_close  

__root__ = None
__rw__ = None

def command_view_all():
    global __rw__

    books = view_all_books()

    print(books)

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
    title_length = box_length - isbn_length - author_length - year_length - 7 # 5 is for a space between each and quotes around title

    __rw__.book_listbox.delete(0, __rw__.book_listbox.size())
    for index, book in enumerate(books, 1):
        (isbn, title, author, year) = book

        title = title.strip()
        title = title if len(title) < title_length else (title[:(title_length - 3)] + '...') 
        title = "'" + title + "'"

        __rw__.book_listbox.insert(index, f"{isbn:{isbn_length}} {title:{title_length}} {author:{author_length}} ({year:{year_length}})")

def command_search():
    pass

def command_insert():
    try:
        new_isbn = int(__rw__.book_isbn_entry_string.get())
    except:
        return
    
    try:
        new_year = int(__rw__.book_year_entry_string.get())
    except:
        return

    new_title = __rw__.book_title_entry_string.get()
    new_author = __rw__.book_author_entry_string.get()

    insert_book(new_isbn, new_title, new_author, new_year)
    command_view_all()

def command_update():
    pass

def command_delete():
    pass

def command_close():
    pass

def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        __root__.destroy()

def main():
    global __root__
    global __rw__

    db_connect()

    __root__ = Tk()
    __root__.title("BookStore")
    __root__.resizable(width=False, height=False)    
    
    __rw__ = BookWindow(__root__)
    BookWindow.bind_command(__rw__.button_view_command, command_view_all)
    BookWindow.bind_command(__rw__.button_add_entry_command, command_insert)

    command_view_all()

    __root__.protocol("WM_DELETE_WINDOW", on_closing)
    __root__.mainloop()
 
if __name__ == '__main__':
    main()