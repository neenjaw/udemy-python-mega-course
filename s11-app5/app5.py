from tkinter import *
from tkinter import ttk

window = Tk()

def km_to_miles(km):
    return float(km) / 1.6

def execute_km_to_mi():
    try:
        new_value = "{0:.5f} mi".format(km_to_miles(entry_km_value.get()))
    except:
        new_value = "Unable to convert."

    text_mi.delete("1.0", END)
    text_mi.insert(END,new_value)

window.title("Library Application")
window.resizable(width=False, height=False)

mainframe = ttk.Frame(window, height=50, width=300)
mainframe.grid(column=0, row=0, padx=12, pady=12, sticky=(N, W, E, S))
window.columnconfigure(0, minsize=150, weight=1)
window.rowconfigure(0, weight=1)

entry_km_value=StringVar()
entry_km = ttk.Entry(mainframe, textvariable=entry_km_value)
entry_km.grid(row=0, column=0, padx=(0, 12), sticky=(N, W, E, S))

text_mi = Text(mainframe, width=20, height=1)
text_mi.grid(row=0, column=1, padx=(0,12), sticky=(N, W, E, S))


button_execute = ttk.Button(mainframe, text="Execute", command=execute_km_to_mi)
button_execute.grid(row=0, column=3, sticky=(N, W, E, S))

window.mainloop()
