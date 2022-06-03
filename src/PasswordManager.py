import pickle
from src import Credential, Encryption
import os


class PasswordManager:

    def __init__(self):
        """

        """
        try:
            dict_file = open("data.pkl", "rb")
            self.Dict = pickle.load(dict_file)
            dict_file.close()
        except (OSError, IOError) as e:
            test = dict()
            dict_file = open("data.pkl", "wb")
            pickle.dump(test, dict_file)
            self.Dict = dict()
            dict_file.close()

    def add_credential(self, website, username, len_password, lower_case=True,
                       upper_case=True, special_char=True, digits=True):
        """
        This function adds a randomly generated password to the corresponding
        username and website

        :param website: str containing the website url
        :param username: str containing the username
        :param len_password: int containing the desired length of the password
        :param lower_case: boolean indicating if lowercase letters should be present
        :param upper_case: boolean indicating if uppercase letters should be present
        :param special_char: boolean indicating if special characters should be present
        :param digits: boolean indicating if digits should be present

        :return: generated password to corresponding website and username
        """
        self.Dict[website] = Credential.Credential(username, len_password, lower_case,
                                        upper_case,special_char,digits)

        with open("data.pkl", "wb") as dict_file:
            pickle.dump(self.Dict, dict_file)

        dict_file.close()

    def find_password(self, website):
        """
        This function returns the password generated for a specific website

        :param website: str containing website user want to know the password of

        :return: found password
        """
        enc = Encryption.Encryption()

        return enc.decrypt(self.Dict[website].password)

    def show_username(self, website):
        """
        Show the username corresponding to the website
        :param website: str containing the website name
        :return: str containing the username
        """
        return self.Dict[website].username
