import pickle
from src import Credential


class PasswordManager:

    def __init__(self):
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
        # filter = input("How long: \n")
        self.add_credential(website, username)

    def add_credential(self, website, username):
        """
        This function adds a randomly generated password to the corresponding
        username and website

        :param website: str containing the website url
        :param username: str containing the username

        :return: generated password to corresponding website and username
        """
        self.Dict[website] = Credential(username)

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

        return self.Dict[website]



