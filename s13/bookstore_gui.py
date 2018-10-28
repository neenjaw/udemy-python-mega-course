"""
An application to manage a bookstore repository
"""

from tkinter import *
from tkinter import ttk
from tkinter import font

class BookWindow():
    def __init__(self, parent):
        self.parent = parent

        """
        The upper book area
        """

        self.book_frame_style = ttk.Style()
        self.book_frame_style.configure("My.TFrame")
        self.book_frame = ttk.Frame(self.parent, style="My.TFrame", border=1)
        self.book_frame.grid(column=0, row=0, columnspan=2, padx=(12,12), pady=(12,6), sticky=(N, W, E, S))
        self.book_frame.columnconfigure(1, weight=1)
        self.book_frame.columnconfigure(3, weight=1)

        # Book title
        # Label
        self.book_title_label_string = StringVar()
        self.book_title_label_string.set("Book Title:")
        self.book_title_label = ttk.Label(self.book_frame, textvariable=self.book_title_label_string)
        self.book_title_label.grid(row=0, column=0, padx=(0,6), pady=(0,6), sticky=(N, E))

        # Entry
        self.book_title_entry_string = StringVar()
        self.book_title_entry = ttk.Entry(self.book_frame, textvariable=self.book_title_entry_string)
        self.book_title_entry.grid(row=0, column=1, padx=(0,6), pady=(0,6), sticky=(N, E, W))

        # Book author
        # Label
        self.book_author_label_string = StringVar()
        self.book_author_label_string.set("Author:")
        self.book_author_label = ttk.Label(self.book_frame, textvariable=self.book_author_label_string)
        self.book_author_label.grid(row=0, column=2, padx=(0,6), pady=(0,6), sticky=(N, E))
        
        # Entry
        self.book_author_entry_string = StringVar()
        self.book_author_entry = ttk.Entry(self.book_frame, textvariable=self.book_author_entry_string)
        self.book_author_entry.grid(row=0, column=3, padx=(0,0), pady=(0,6), sticky=(N, E, W))

        # Book Year
        # Label
        self.book_year_label_string = StringVar()
        self.book_year_label_string.set("Year:")
        self.book_year_label = ttk.Label(self.book_frame, textvariable=self.book_year_label_string, anchor="e")
        self.book_year_label.grid(row=1, column=0, padx=(0,6), pady=(0,6), sticky=(N, E))

        # Entry
        self.book_year_entry_string = StringVar()
        self.book_year_entry = ttk.Entry(self.book_frame, textvariable=self.book_year_entry_string)
        self.book_year_entry.grid(row=1, column=1, padx=(0,6), pady=(0,0), sticky=(N, E, W))
        
        # Book isbn
        # Label
        self.book_isbn_label_string = StringVar()
        self.book_isbn_label_string.set("ISBN:")
        self.book_isbn_label = ttk.Label(self.book_frame, textvariable=self.book_isbn_label_string, anchor="e")
        self.book_isbn_label.grid(row=1, column=2, padx=(0,6), pady=(0,0), sticky=(N, E))
        
        # Entry
        self.book_isbn_entry_string = StringVar()
        self.book_isbn_entry = ttk.Entry(self.book_frame, textvariable=self.book_isbn_entry_string)
        self.book_isbn_entry.grid(row=1, column=3, padx=(0,0), pady=(0,0), sticky=(N, E, W))
        
        """
        The lower left listbox area
        """
        
        self.listbox_frame = ttk.Frame(self.parent)
        self.listbox_frame.grid(column=0, row=1, padx=(12,6), pady=(6,12), sticky=(N, W, E, S))
        self.listbox_frame.rowconfigure(0, weight=1)
        
        self.book_listbox_scrollbar = Scrollbar(self.listbox_frame)
        self.book_listbox_scrollbar.grid(row=0, column=1, padx=(2,6), sticky=(N,S,))

        self.book_listbox_font = font.Font(family="Courier", size=12)

        self.book_listbox = Listbox(
            self.listbox_frame, 
            height=10, 
            width=80, 
            yscrollcommand=self.book_listbox_scrollbar.set, 
            font=self.book_listbox_font)
        self.book_listbox.grid(row=0, column=0, sticky=(N,E,W,S,))
        
        """
        The lower right command box
        """
        
        self.command_button_frame = ttk.Frame(self.parent)
        self.command_button_frame.grid(column=1, row=1, padx=(6,12), pady=(6,12), sticky=(N,E,W,S,))
        
        self.button_view_command = ttk.Button(self.command_button_frame, text="View all")
        self.button_view_command.grid(row=0, column=0, pady=(0,6), sticky=(W, E,))
        
        self.button_search_command = ttk.Button(self.command_button_frame, text="Search")
        self.button_search_command.grid(row=1, column=0, pady=(0,6), sticky=(W, E,))
        
        self.button_add_entry_command = ttk.Button(self.command_button_frame, text="Add entry")
        self.button_add_entry_command.grid(row=2, column=0, pady=(0,6), sticky=(W, E,))
        
        self.button_update_command = ttk.Button(self.command_button_frame, text="Update")
        self.button_update_command.grid(row=3, column=0, pady=(0,6), sticky=(W, E,))
        
        self.button_delete_command = ttk.Button(self.command_button_frame, text="Delete")
        self.button_delete_command.grid(row=4, column=0, pady=(0,6), sticky=(W, E,))
        
        self.button_close_command = ttk.Button(self.command_button_frame, text="Close")
        self.button_close_command.grid(row=5, column=0, sticky=(W, E,))

    def bind_command(item, new_command):
        return item.configure(command=new_command)
    
"""
The main call
"""

def main():
    root = Tk()
    root.title("BookStore")
    root.resizable(width=False, height=False)    
    rw = BookWindow(root)
    root.mainloop()
 
 
if __name__ == '__main__':
    main()