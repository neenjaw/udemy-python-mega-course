from tkinter import *
from tkinter import ttk

window = Tk()
window.title("Library Application")

mainframe = ttk.Frame(window, height=200, width=500)
mainframe.grid(column=0, row=0, padx=12, pady=12, sticky=(N, W, E, S))
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)

b1 = ttk.Button(mainframe, text="Execute")
b1.grid(row=0, column=0)

e1 = ttk.Entry(mainframe)
e1.grid(row=0, column=1, padx=(12, 0))

t1 = Text(mainframe)
t1.grid(column=0, row=1, columnspan=2, pady=(0,12))

window.mainloop()
