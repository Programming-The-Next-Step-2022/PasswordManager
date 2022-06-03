import unittest

from src.SetupKey import SetupKey

class TestValidateKey(unittest.TestCase):

    def test_validation(self):
        """
        Test whether master password is typed correctly the second time

        :return: boolean
        """
        setupkey = SetupKey()
        self.assertTrue(setupkey.validate_key('test', 'test'))

if __name__ == '__main__':
    unittest.main()
