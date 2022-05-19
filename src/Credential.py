# """
# Generate a random password of x characters long
# """
import random
import string


class Credential:
    """
    This class contains the credentials for a website
    """

    def __init__(self, username):
        self.username = username
        self.password = self.generate_password()

    def __repr__(self):
        return "\n'username' = " + self.username + "\n'password' = " + self.password + "\n"

    def __str__(self):
        return self.__repr__()

    def generate_password(self):
        """
        This function generates a password of random length containing random
        characters

        :return: a password of random length with random characters
        """
        len_password = random.randint(13, 25)
        all_characters = list(
            string.ascii_letters + string.digits + "!@#$%^&*()")
        password = ''.join(random.choices(all_characters, k=len_password))

        return password
