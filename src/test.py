import pickle



# dict_file = open("data.pkl", "wb")
# pickle.dump(Dict, dict_file)
# dict_file.close()
from src import Credential


class PasswordManager:

    def __init__(self):
        self.Dict = {}

        # dict_file.close()

    def init_input(self):
        """
        This functions asks the user for website and username and saves it in a
        dictionary
        """
        website = input("Website: \n")
        username = input("Username: \n")
        # dict_file = open("data.pkl", "wb")
        self.Dict[website] = Credential(username)
        # pickle.dump(self.Dict, dict_file)
        # dict_file.close()

    def find_password(self, website):
        """
        This function returns the password generated for a specific website

        :param Dict: dictionary containing the passwords
        :param website: str containing website user want to know the password of

        :return: found password
        """
        # dict_file = open("data.pkl", "rb")
        # loaded_dict = pickle.load(dict_file)
        # found_password = loaded_dict[website]
        # print(found_password)
        # dict_file.close()
        return self.Dict[website]



