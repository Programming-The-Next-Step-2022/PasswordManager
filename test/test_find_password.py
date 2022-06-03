import unittest

from src.PasswordManager import PasswordManager
from src import Encryption


class TestFindPassword(unittest.TestCase):

    def test_password_not_none(self):
        """
        This unittest tests if a password is generated

        :return: boolean indicating if password is generated
        """
        password_manager = PasswordManager()
        password_manager.add_credential('testweb', 'testuser', 15, lower_case=True,
                                        upper_case=True, digits=True, special_char=True)
        self.assertIsNotNone(password_manager.find_password('testweb'))

    def test_right_password(self):
        """
        Test whether found password is the same as generated password

        :return: boolean indicating whether found password is same as generated
        password
        """
        password_manager = PasswordManager()
        enc = Encryption.Encryption()
        password_manager.add_credential('testweb', 'testuser', 15, lower_case=True,
                                        upper_case=True, digits=True, special_char=True)
        self.assertEqual(enc.decrypt(password_manager.Dict['testweb'].password), password_manager.find_password('testweb'))


if __name__ == '__main__':
    unittest.main()
