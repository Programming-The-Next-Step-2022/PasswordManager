import tkinter.messagebox as tm
from tkinter import *
from tkinter.ttk import *
from os.path import exists

from src import Login, Credential, Encryption, PasswordManager, SetupKey
from src import *

window = Tk()
window.title("Password Manager")
window.geometry("700x250")


# Create row
# window.columnconfigure([0], minsize=20)
# window.rowconfigure([0, 1], minsize=20)

# Make label

def find_password(website, password_label, window, textbox):
    textbox.delete('1.0', END)

    try:
        password_manager = PasswordManager.PasswordManager()
        found_password = password_manager.find_password(website)
        # textbox.insert(password_label.config(text=found_password))
        # Text(window, password_label.config(text=found_password), width=50, height=3, wrap=WORD).pack()
    except:
        tm.showerror("Find password error", "Could not find password")
    else:
        textbox.insert(END, found_password)


# # Define a function to return the Input data
# def get_data():
#    label.config(text= website_entry.get())

def find_password_screen():
    find_password_scrn = Toplevel(window)
    find_password_scrn.geometry("700x250")
    find_password_scrn.title("Find Password")
    website_label = Label(find_password_scrn, text="Website")

    website_entry = Entry(find_password_scrn)
    website_entry.place(relx=.5, rely=.5, anchor=CENTER)
    # website = website_entry.get()
    # website_entry.pack()
    # Inititalize a Label widget
    label = Label(find_password_scrn, text="")

    button_click = Button(find_password_scrn, text="Search",
                          command=lambda: label.config(
                              text=find_password(website_entry.get(), label,
                                                 find_password_scrn, output)))
    output = Text(find_password_scrn, width=40, height=1)

    website_label.pack()
    website_entry.pack()
    button_click.pack()
    label.pack()
    output.pack()
    # print(website_entry.get())
    # password_label = Label(find_password_scrn)


def generate_password(textbox, website, username, length_password,
                      lower_case=True, upper_case=True, digits=True,
                      special_char=True):
    try:
        textbox.delete('1.0', END)
        password_manager = PasswordManager.PasswordManager()
        password_manager.add_credential(website, username, int(length_password),
                                        lower_case, upper_case, digits,
                                        special_char)
        found_password = password_manager.find_password(website)
        textbox.insert(END, found_password)
        # textbox.insert(password_label.config(text=found_password))
        # Text(window, password_label.config(text=found_password), width=50, height=3, wrap=WORD).pack()
    except ValueError as error:
        tm.showerror("Find password error", "Could not find password")


def generate_password_screen():
    generate_password_scrn = Toplevel(window)
    generate_password_scrn.geometry("900x300")
    generate_password_scrn.title("Find Password")
    website_label = Label(generate_password_scrn, text="Website")
    website_entry = Entry(generate_password_scrn)
    # website = website_entry.get()
    username_label = Label(generate_password_scrn, text="Username")
    username_entry = Entry(generate_password_scrn)
    # username = username_entry.pack()
    length_label = Label(generate_password_scrn, text="Length of password")
    length_entry = Entry(generate_password_scrn)
    # username = username_entry.pack()
    # label = Label(generate_password_scrn, text="")

    boolvar_dig = BooleanVar()
    boolvar_dig.set(True)

    boolvar_uc = BooleanVar()
    boolvar_uc.set(True)
    boolvar_lc = BooleanVar()
    boolvar_lc.set(True)
    boolvar_sc = BooleanVar()
    boolvar_sc.set(True)

    cb_digit = Checkbutton(generate_password_scrn, text="Digits",
                           variable=boolvar_dig)
    cb_uppercase = Checkbutton(generate_password_scrn, text="Uppercase",
                               variable=boolvar_uc)
    cb_lowercase = Checkbutton(generate_password_scrn, text="Lowercase",
                               variable=boolvar_lc)
    cb_specialchar = Checkbutton(generate_password_scrn,
                                 text="Special Characters", variable=boolvar_sc)

    button_click = Button(generate_password_scrn, text="Generate",
                          command=lambda: generate_password(output,
                                                            website_entry.get(),
                                                            username_entry.get(),
                                                            length_entry.get(),
                                                            boolvar_lc.get(),
                                                            boolvar_uc.get(),
                                                            boolvar_dig.get(),
                                                            boolvar_sc.get()))
    output = Text(generate_password_scrn, width=40, height=1)

    website_label.pack()
    website_entry.pack()
    username_label.pack()
    username_entry.pack()
    length_label.pack()
    length_entry.pack()
    cb_digit.pack()
    cb_uppercase.pack()
    cb_lowercase.pack()
    cb_specialchar.pack()
    button_click.pack()
    output.pack()


def login_button_clicked():
    master_password = entry_masterpassword.get()
    login = Login.Login()

    if login.login(master_password):
        new_window = Toplevel(window)
        new_window.geometry("700x250")
        new_window.title("Password Manager")

        Label(new_window, text="Choose option:").pack()
        Button(new_window, text="Find Password",
               command=find_password_screen).pack()
        Button(new_window, text="Generate Password",
               command=generate_password_screen).pack()
    else:
        tm.showerror("Login error", "Incorrect Master password")


def init_master_password(master_password, repeat_password):
    setupkey = SetupKey.SetupKey()
    try:
        setupkey.validate_key(master_password, repeat_password)
    except:
        tm.showerror("Initialize master password", "Not the same password")
    else:
        setupkey.init_key(master_password, repeat_password)





if __name__ == '__main__':

    if exists("key.txt"):

        Label(text="Fill in your master password ").pack()

        Label(text="Master password: ").pack()
        # master_password = StringVar()
        entry_masterpassword = Entry(show="*")
        master_password = entry_masterpassword.get()
        entry_masterpassword.pack()
        Button(text="Login", command=login_button_clicked).pack()
    # print(login.login(master_password))
    # label_title.grid(row=0, column=0, sticky="w", padx=5, pady=5)
    # label_master.grid(row=1, column=0, sticky="w", padx=5, pady=5)
    #
    else:
        pass
        # first_mp_label = Label(text="Fill in your masterpassword: ")
        # repeat_mp_label = Label(text="Fill in your masterpassword again: ")
        #
        # first_mp_entry = Entry(show="*")
        # repeat_mp_entry = Entry(show="*")
        #
        # button_click = Button(text="Submit", command=init_master_password(first_mp_entry.get(), repeat_mp_entry.get()))
        #
        # first_mp_label.pack()
        # first_mp_entry.pack()
        # repeat_mp_label.pack()
        # repeat_mp_entry.pack()

    window.mainloop()
