import unittest

from src.Encryption import Encryption


class TestEncryption(unittest.TestCase):

    def test_decryption(self):
        """
        Test whether decrypted password is the same as original password

        :return: boolean indicating if decrypted password is same as original
        """
        crypto = Encryption('testkey')
        enc = crypto.encrypt('test')
        self.assertEqual('test', crypto.decrypt(enc))

    def test_decryption_not_none(self):
        """
        Test whether password is decrypted

        :return: boolean indicating if password is decrypted
        """
        crypto = Encryption('testkey')
        enc = crypto.encrypt('test')
        self.assertIsNotNone(crypto.decrypt(enc))


if __name__ == '__main__':
    unittest.main()
