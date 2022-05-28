# import tkinter as tk
# import tkinter.ttk as ttk
from tkinter import *
from tkinter.ttk import *

import src.Login
from src import *

window = Tk()
window.title("Password Manager")

# Create row
# window.columnconfigure([0], minsize=20)
# window.rowconfigure([0, 1], minsize=20)

# Make label
login = src.Login.Login()
Label(text="Fill in your master password ").pack()
Label(text="Master password: ").pack()
entry_masterpassword = Entry()
master_password = entry_masterpassword.get()
login.login()
entry_masterpassword.pack()
# label_title.grid(row=0, column=0, sticky="w", padx=5, pady=5)
# label_master.grid(row=1, column=0, sticky="w", padx=5, pady=5)
#

window.mainloop()