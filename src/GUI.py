# # import tkinter as tk
# # import tkinter.ttk as ttk
# import tkinter.messagebox as tm
# from os import path
# from tkinter import *
# from tkinter.ttk import *
# from functools import partial
#
# from src import Login, SetupKey, PasswordManager
# from src import *
#
# window = Tk()
# window.geometry("750x250")
# window.title("Password Manager")
#
#
# # Create row
# # window.columnconfigure([0], minsize=20)
# # window.rowconfigure([0, 1], minsize=20)
#
# # Make label
#
# def welcome_new_user():
#     window.geometry("450x200")
#
#     label1 = Label(window, text="Create New Master Password")
#     label1.config(anchor=CENTER)
#     label1.pack(pady=10)
#
#     mp_entry_box = Entry(window, width=20, show="*")
#     master_password = mp_entry_box.get()
#     mp_entry_box.pack()
#     mp_entry_box.focus()
#
#     label2 = Label(window, text="Enter the password again")
#     label2.config(anchor=CENTER)
#     label2.pack(pady=10)
#
#     rmp_entry_box = Entry(window, width=20, show="*")
#     repeat_master_password = rmp_entry_box.get()
#     rmp_entry_box.pack()
#
#     feedback = Label(window)
#     feedback.pack()
#
#     save_btn = Button(window, text="Create Password")
#     save_btn.pack(pady=5)
#
#     return master_password, repeat_master_password
#
#
# def validate_masterpassword(master_password, repeat_mp):
#     pass
#
#
# def login_button_clicked():
#     master_password = entry_masterpassword.get()
#     login = Login.Login()
#
#     if login.login(master_password):
#         new_window = Toplevel(window)
#         new_window.title("Password Manager")
#         Button(text="Find Password").pack()
#
#     else:
#         tm.showerror("Login error", "Incorrect Login details")
#     #
#     # if login.login(master_password):
#     #     new_window = Toplevel(window)
#     #     new_window.geometry("700x250")
#     #     new_window.title("Password Manager")
#     #     # new_window.grab_set()
#     #     # Label(new_window, text="Choose option:").pack()
#     #     # Button(new_window, text="Find Password", command=lambda: Toplevel(new_window)).pack()
#     # else:
#     #     tm.showerror("Login error", "Incorrect Login details")
#
# Label(text="Fill in your master password ").pack()
# Label(text="Master password: ").pack()
# # master_password = StringVar()
# entry_masterpassword = Entry(show="*")
# master_password = entry_masterpassword.get()
# entry_masterpassword.pack()
# Button(text="Login", command=login_button_clicked()).pack()
#
# # Label(text="Fill in your master password ").pack()
# # Label(text="Master password: ").pack()
# # # master_password = StringVar()
# # entry_masterpassword = Entry(show="*")
# # entry_masterpassword.pack()
# # Button(text="Login", command=login_button_clicked()).pack()
# # master_password = entry_masterpassword.get()
# # #
# # def login_screen():
# #     Label(text="Fill in your master password ").pack()
# #     Label(text="Master password: ").pack()
# #     master_password = StringVar()
# #     entry_masterpassword = Entry(show="*", textvariable=master_password)
# #     master_password = master_password.get()
# #     entry_masterpassword.pack()
# #
# #     Button(text="Login", command=login_button_clicked(master_password)).pack()
# #
# #
# # # Label(text="Choose option:").pack()
# # # Button(text="Find Password", command=lambda: Toplevel(new_window)).pack()
# #
# #
# # # print(login.login(master_password))
# # # label_title.grid(row=0, column=0, sticky="w", padx=5, pady=5)
# # # label_master.grid(row=1, column=0, sticky="w", padx=5, pady=5)
# # #
# #
# # if __name__ == '__main__':
# #
# #     if path.exists("key.txt"):
# #         login_screen()
# #     else:
# #         welcome_new_user()
# #
# window.mainloop()

###############################################################################
# import tkinter as tk
# import tkinter.ttk as ttk
import tkinter.messagebox as tm
from tkinter import *
from tkinter.ttk import *

from src import Login, Credential, Encryption, PasswordManager
from src import *

window = Tk()
window.title("Password Manager")

# Create row
# window.columnconfigure([0], minsize=20)
# window.rowconfigure([0, 1], minsize=20)

# Make label

def find_password(website):

    try:
        password_manager = PasswordManager.PasswordManager()
        found_password = password_manager.find_password(website)
        # password_label.config(text=found_password)
    except ValueError as error:
        tm.showerror("Find password error", "Could not find password")

# Define a function to return the Input data
def get_data():
   label.config(text= website_entry.get(), font= ('Helvetica 13'))

def find_password_screen():
    find_password_scrn = Toplevel(window)
    find_password_scrn.geometry("700x250")
    find_password_scrn.title("Find Password")
    Label(find_password_scrn, text="Website").pack()
    website = StringVar()
    website_entry = Entry(find_password_scrn)
    website_entry.place(relx=.5, rely=.5, anchor=CENTER)
    # website = website_entry.get()
    # website_entry.pack()
    # Inititalize a Label widget
    label = Label(find_password_scrn, text="", font=('Helvetica 13'))
    label.pack()
    Button(find_password_scrn, text="Submit", command=lambda:  label.config(text=find_password(website_entry.get()), font= ('Helvetica 13'))).pack()
    print(website_entry.get())
    # password_label = Label(find_password_scrn)


def generate_password_screen():
    generate_password_scrn = Toplevel(window)
    generate_password_scrn.geometry("700x250")
    generate_password_scrn.title("Find Password")
    Label(generate_password_scrn, text="Website").pack()
    website_entry = Entry(generate_password_scrn).pack()
    # website = website_entry.get()
    Label(generate_password_scrn, text="Username").pack()
    username_entry = Entry(generate_password_scrn).pack()
    # username = username_entry.pack()



def login_button_clicked():
    master_password = entry_masterpassword.get()
    login = Login.Login()


    if login.login(master_password):
        new_window = Toplevel(window)
        new_window.geometry("700x250")
        new_window.title("Password Manager")

        Label(new_window, text="Choose option:").pack()
        Button(new_window, text="Find Password", command=find_password_screen).pack()
        Button(new_window, text="Generate Password", command=generate_password_screen).pack()
    else:
        tm.showerror("Login error", "Incorrect Login details")


Label(text="Fill in your master password ").pack()
Label(text="Master password: ").pack()
# master_password = StringVar()
entry_masterpassword = Entry(show="*")
master_password = entry_masterpassword.get()
entry_masterpassword.pack()
Button(text="Login", command=login_button_clicked).pack()

print(master_password)
# print(login.login(master_password))
# label_title.grid(row=0, column=0, sticky="w", padx=5, pady=5)
# label_master.grid(row=1, column=0, sticky="w", padx=5, pady=5)
#




window.mainloop()