from tkinter import *
from tkinter import ttk

root = Tk()

root.title("BookStore")
root.resizable(width=False, height=False)

book_frame = ttk.Frame(root)
book_frame.grid(column=0, row=0, padx=(12,12), pady=(12,6), sticky=(N, W, E, S))

# Book title
# Label
book_title_label_string = StringVar()
book_title_label_string.set("Book Title:")
book_title_label = ttk.Label(book_frame, textvariable=book_title_label_string)
book_title_label.grid(row=0, column=0, padx=(0,6), pady=(0,6), sticky=(N, W))

# Entry
book_title_entry_string = StringVar()
book_title_entry = ttk.Entry(book_frame, textvariable=book_title_entry_string)
book_title_entry.grid(row=0, column=1, padx=(0,6), pady=(0,6), sticky=(N, W))

# Book Year
# Label
book_year_label_string = StringVar()
book_year_label_string.set("Year:")
book_year_label = ttk.Label(book_frame, textvariable=book_year_label_string, anchor="e")
book_year_label.grid(row=1, column=0, padx=(0,6), pady=(0,6), sticky=(N, W))

# Entry
book_year_entry_string = StringVar()
book_year_entry = ttk.Entry(book_frame, textvariable=book_year_entry_string)
book_year_entry.grid(row=1, column=1, padx=(0,6), pady=(0,0), sticky=(N, W))


# Book author
# Label
book_author_label_string = StringVar()
book_author_label_string.set("Author:")
book_author_label = ttk.Label(book_frame, textvariable=book_author_label_string)
book_author_label.grid(row=0, column=2, padx=(0,6), pady=(0,6), sticky=(N, W))

# Entry
book_author_entry_string = StringVar()
book_author_entry = ttk.Entry(book_frame, textvariable=book_author_entry_string)
book_author_entry.grid(row=0, column=3, padx=(0,0), pady=(0,6), sticky=(N, W))

# Book isbn
# Label
book_isbn_label_string = StringVar()
book_isbn_label_string.set("ISBN:")
book_isbn_label = ttk.Label(book_frame, textvariable=book_isbn_label_string, anchor="e")
book_isbn_label.grid(row=1, column=2, padx=(0,6), pady=(0,0), sticky=(N, W))

# Entry
book_isbn_entry_string = StringVar()
book_isbn_entry = ttk.Entry(book_frame, textvariable=book_isbn_entry_string)
book_isbn_entry.grid(row=1, column=3, padx=(0,0), pady=(0,0), sticky=(N, W))

root.mainloop()