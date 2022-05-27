from src import SetupKey


class Login:
    def __init__(self):
        self.key = SetupKey.SetupKey().key.decode("utf-8")

    def login(self):
        """
        Check whether the login password is the same as the master password

        :return: boolean indicating if the login password is the same as the
        master password.
        """
        master_password = input("Please enter your master password: \n")

        return master_password == self.key



