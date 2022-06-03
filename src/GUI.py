import tkinter.messagebox as tm
from tkinter import *
from tkinter.ttk import *
from os.path import exists

# from src import Login, Credential, Encryption, PasswordManager, SetupKey
from src import *

# Create root window
window = Tk()
window.title("Password Manager")
window.geometry("700x250")


def find_password(website, textbox_password, textbox_username):
    """
    Find the password given a website and return it in a textbox.
    Returns an error if the password is not found

    :param website: str containing the website name
    :param textbox_password: textbox in which the password should be shown
    :param textbox_username: textbox in which the username should be shown
    :return: textbox containing password
    """
    # Clear the textbox
    textbox_password.delete('1.0', END)
    textbox_username.delete('1.0', END)

    # Try to find the password and put it in a textbox. Otherwise, an error is
    # returned.
    try:
        password_manager = PasswordManager.PasswordManager()
        found_password = password_manager.find_password(website)
        found_username = password_manager.show_username(website)
    except:
        tm.showerror("Find password error", "Could not find password")
    else:
        textbox_password.insert(END, found_password)
        textbox_username.insert(END, found_username)


def find_password_screen():
    """
    Initializes the 'find password' screen. The user can give the website name
    and the password will be returned in the textbox, if it exists.

    :return: a new window
    """
    find_password_scrn = Toplevel(window)
    find_password_scrn.geometry("900x300")
    find_password_scrn.title("Find Password")
    find_password_scrn.grab_set()

    website_label = Label(find_password_scrn, text="Website")
    website_entry = Entry(find_password_scrn)
    website_entry.place(relx=.5, rely=.5, anchor=CENTER)

    # Initialize a Label widget so the user can input a website
    label = Label(find_password_scrn, text="")
    button_click = Button(find_password_scrn, text="Search",
                          command=lambda: label.config(
                              text=find_password(website_entry.get(), output,
                                                 output_username)))

    # Create textbox in which the password will be shown
    username_label = Label(find_password_scrn, text="Username: ")
    output = Text(find_password_scrn, width=40, height=1)
    password_label = Label(find_password_scrn, text="Password: ")
    output_username = Text(find_password_scrn, width=40, height=1)

    website_label.pack()
    website_entry.pack(pady=10)
    button_click.pack()
    label.pack()
    username_label.pack(pady=5)
    output_username.pack(pady=10)
    password_label.pack(pady=10)
    output.pack()


def generate_password(textbox, website, username, length_password,
                      lower_case=True, upper_case=True, digits=True,
                      special_char=True):
    """
    Generate a password given the user's input

    :param textbox: textbox in which the password will be printed
    :param website: str containing the website name
    :param username: str containing the username
    :param length_password: str containing the desired length of the password
    :param lower_case: boolean whether lower case letters should be present
    :param upper_case: boolean whether upper case letters should be present
    :param digits: boolean whether digits should be present
    :param special_char: boolean whether special characters should be present
    :return: a generated password based on the user's wishes in a textbox
    """
    try:
        # Clear the textbox
        textbox.delete('1.0', END)
        if not length_password.isdigit():
            raise KeyError("Not an integer")
        if not website or not username or not length_password:
            raise ValueError("empty string")
        if not digits and not upper_case and not lower_case and not special_char:
            raise AssertionError("No input arguments given")
        password_manager = PasswordManager.PasswordManager()
        password_manager.add_credential(website, username, int(length_password),
                                        lower_case, upper_case, digits,
                                        special_char)
        found_password = password_manager.find_password(website)
        textbox.insert(END, found_password)
    except ValueError:
        tm.showerror("Not all fields are filled in",
                     "Not all the fields are filled in,"
                     " please fill all the fields in!")
    except KeyError:
        tm.showerror("Not a number given", "Please fill a number in for desired length!")
    except AssertionError as e:
        tm.showerror("Generate password error", "Check at least one of the boxes!")


def generate_password_screen():
    """
    Generate a screen to ask the user input to generate password
    :return: screen containing input questions
    """
    generate_password_scrn = Toplevel(window)
    generate_password_scrn.geometry("900x300")
    generate_password_scrn.title("Generate Password")
    generate_password_scrn.grab_set()

    website_label = Label(generate_password_scrn, text="Website")
    website_entry = Entry(generate_password_scrn)

    username_label = Label(generate_password_scrn, text="Username")
    username_entry = Entry(generate_password_scrn)

    length_label = Label(generate_password_scrn, text="Length of password")
    length_entry = Entry(generate_password_scrn)

    # Default digit option is True
    boolvar_dig = BooleanVar()
    boolvar_dig.set(True)

    # Default uppercase option is True
    boolvar_uc = BooleanVar()
    boolvar_uc.set(True)

    # Default lowercase option is True
    boolvar_lc = BooleanVar()
    boolvar_lc.set(True)

    # Default special characters option is True
    boolvar_sc = BooleanVar()
    boolvar_sc.set(True)

    # When user starts program, check buttons are all checked
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
    button_click.pack(pady=5)
    output.pack(pady=10)


def login_button_clicked():
    """
    Create a new window when the login button has been clicked.
    User can choose to find a password or generate a password.
    :return: a new window on top of the root window
    """
    master_password = entry_masterpassword.get()
    login = Login.Login()

    if login.login(master_password):

        # Withdraw the root window and create a new window
        # window.withdraw()
        new_window = Toplevel(window)
        new_window.geometry("700x250")
        new_window.title("Password Manager")
        new_window.grab_set()

        Label(new_window, text="Choose option:").pack(pady=10)
        Button(new_window, text="Find Password",
               command=find_password_screen).pack(pady=15)
        Button(new_window, text="Generate Password",
               command=generate_password_screen).pack(pady=15)
    else:
        tm.showerror("Login error", "Incorrect Master password")


def init_master_password(master_password, repeat_password):
    """
    Initialize the user's master password
    :param master_password: str master password
    :param repeat_password: str master password repeated
    :return: message telling the user whether the masterpassword is succesfully
    initiliazed
    """
    try:
        SetupKey.SetupKey(master_password, repeat_password)
    except SyntaxError:
        tm.showerror("Initialize master password", "Not the same password")
    else:
        tm.showinfo("Master password generated",
                    "Master password is succesfully created!")


if __name__ == '__main__':

    # If this is not the first time the user logs in, a login screen will popup
    # else, a screen will popup so the user can create a masterpassword.
    if exists("key.txt"):
        Label(text="Fill in your master password ").pack(pady=10)
        Label(text="Master password: ").pack(pady=10)
        entry_masterpassword = Entry(show="*")
        master_password = entry_masterpassword.get()
        entry_masterpassword.pack(pady=5)
        Button(text="Login", command=login_button_clicked).pack()
    else:
        first_mp_label = Label(text="Fill in your masterpassword: ")
        repeat_mp_label = Label(text="Fill in your masterpassword again: ")

        first_mp_entry = Entry(show="*")
        repeat_mp_entry = Entry(show="*")

        button_click = Button(text="Submit",
                              command=lambda: init_master_password(
                                  first_mp_entry.get(),
                                  repeat_mp_entry.get()))
        first_mp_label.pack(pady=5)
        first_mp_entry.pack(pady=5)
        repeat_mp_label.pack(pady=5)
        repeat_mp_entry.pack(pady=5)
        button_click.pack(pady=10)

    window.mainloop()
