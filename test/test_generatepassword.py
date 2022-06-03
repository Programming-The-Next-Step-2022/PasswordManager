import unittest

from src import Encryption
from src.Credential import Credential

class TestValidateKey(unittest.TestCase):

    def test_password_is_length_12(self):
        """
        Test whether master password is length 12, as indicated by user
        """
        password = Credential('test', 12)
        enc = Encryption.Encryption()
        self.assertEqual(len(enc.decrypt(password.password)), 12)

    def test_password_is_numeric(self):
        """
        Test whether password contains only digits if user indicates that
        """
        password = Credential('test', 12, upper_case=False, lower_case=False, special_char=False, digits=True)
        enc = Encryption.Encryption()
        self.assertTrue(enc.decrypt(password.password).isdigit())


if __name__ == '__main__':
    unittest.main()
