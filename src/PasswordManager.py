import pickle
from src import Credential, Encryption
import os


class PasswordManager:

    def __init__(self):
        """
        todo: close file
        """
        # try:
        #     self.Dict = pickle.load(open("data.pkl", "rb"))
        # except (OSError, IOError) as e:
        #     test = dict()
        #     pickle.dump(test, open("data.pkl", "wb"))
        #     self.Dict = dict()
        dict_file = open("data.pkl", "rb")
        self.Dict = pickle.load(dict_file)
        dict_file.close()

    def init_input(self):
        """
        This functions asks the user for website and username and saves it in a
        dictionary
        """
        website = input("Website: \n")
        username = input("Username: \n")
        len_password = int(input("How long should the password be?: \n"))
        lower_case = input("Should there be lower case letters in your "
                           " password? (True/False): \n")
        upper_case = input(
            "Should there be upper case letters in your password? "
            " (True/False): \n")
        digits = input(
            "Should there be digits in your password? (True/False): \n")
        special_char = input(
            "Should there be special characters in your password? "
            " (True/False): \n")
        lower_case = self.check_boolean(lower_case)
        upper_case = self.check_boolean(upper_case)
        digits = self.check_boolean(digits)
        special_char = self.check_boolean(special_char)

        self.add_credential(website, username, len_password, lower_case,
                            upper_case, digits, special_char)

    def add_credential(self, website, username, len_password, lower_case=True,
                       upper_case=True, special_char=True, digits=True):
        """
        This function adds a randomly generated password to the corresponding
        username and website

        :param website: str containing the website url
        :param username: str containing the username

        :return: generated password to corresponding website and username
        """
        self.Dict[website] = Credential(username, len_password, lower_case,
                                        upper_case,special_char,digits)

        with open("data.pkl", "wb") as dict_file:
            pickle.dump(self.Dict, dict_file)

        dict_file.close()
        print(self.Dict)

    def find_password(self, website):
        """
        This function returns the password generated for a specific website

        :param website: str containing website user want to know the password of

        :return: found password
        """
        enc = Encryption.Encryption()

        return enc.decrypt(self.Dict[website].password)

    def check_boolean(self, response):
        if response == "True":
            return True
        if response == "False":
            return False
