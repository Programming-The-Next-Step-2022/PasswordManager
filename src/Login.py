from src import SetupKey


class Login:
    def __init__(self):
        self.key = SetupKey.SetupKey()
        while True:
            self.login()

    def login(self):
        master_password = input("Please enter your master password: \n")

        return master_password == self.key


