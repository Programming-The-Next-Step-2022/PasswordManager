# """
# Generate a random password of x characters long
# """
import random
import string

from src import Encryption


class Credential:
    """
    This class contains the credentials for a website
    """

    def __init__(self, username, len_password, lower_case=True, upper_case=True,
                 digits=True, special_char=True):
        self.username = username
        self.len_password = len_password
        self.lower_case = lower_case
        self.upper_case = upper_case
        self.digits = digits
        self.special_char = special_char
        self.password = self.generate_password()

    def __repr__(self):
        return "\n'username' = " + self.username + "\n'password' = " + \
               str(self.password) + "\n"

    def __str__(self):
        return self.__repr__()

    def generate_password(self):
        """
        This function generates a password of random length containing random
        characters

        :return: an encoded password of random length with random characters
        """

        all_characters = list()
        if self.lower_case:
            all_characters.extend(string.ascii_lowercase)
        if self.upper_case:
            all_characters.extend(string.ascii_uppercase)
        if self.special_char:
            all_characters.extend("!@#$%^&*()")
        if self.digits:
            all_characters.extend(string.digits)

        password = ''.join(random.choices(all_characters, k=self.len_password))

        print("123password")
        print(password)

        enc = Encryption.Encryption()
        enc_password = enc.encrypt(password)

        print("321password")
        print(enc_password)

        return enc_password
