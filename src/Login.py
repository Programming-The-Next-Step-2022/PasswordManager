import bcrypt

from src import SetupKey


class Login:
    def __init__(self):
        self.key = SetupKey.SetupKey().key

    def login(self, master_password):
        """
        Check whether the login password is the same as the master password

        :return: boolean indicating if the login password is the same as the
        master password.
        """

        return self.check_password(master_password)

    def check_password(self, password):
        """
        Check whether the given password is the same as the hashed master key
        :param password: str containing the given password during login
        :return: boolean if given master key and actual master key are the same
        """

        return bcrypt.checkpw(password.encode('utf8'), self.key)




