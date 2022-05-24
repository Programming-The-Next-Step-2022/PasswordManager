import base64
import hashlib
from Crypto.Cipher import AES
from Crypto import Random
from src import SetupKey


class Encryption:

    def __init__(self):
        # Use the master key as key to encrypt the passwords
        master_key = SetupKey.SetupKey().key.decode("utf-8")

        self.key = hashlib.sha256(master_key.encode()).digest()
        self.blocksize = AES.block_size

    def pad(self, string):
        """
        Pad the password string until it is a multiple of 16

        :param string: str containing the password
        :return: padded password
        """
        return string + (self.blocksize - len(string) % self.blocksize) * chr(
            self.blocksize - len(string) % self.blocksize)

    def unpad(self, string):
        """
        Remove the padding
        :param string: padded string
        :return: unpadded string
        """
        return string[:-ord(string[len(string) - 1:])]

    def encrypt(self, password):
        """
        Encrypt the password according to AES by using the key
        :rtype: object
        :param password: str containing the password
        :return: encrypted password
        """
        padded_password = self.pad(password)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(padded_password.encode()))

    def decrypt(self, encoded_password):
        """
        Decrypt the AES-encrypted password using the key
        :param encoded_password: encoded and padded password
        :return: decoded and unpadded password
        """
        encoded_password = base64.b64decode(encoded_password)
        iv = encoded_password[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)

        print("meuk123")
        troep = self.unpad(cipher.decrypt(encoded_password[AES.block_size:]))
        print(troep)
        return troep.decode("utf-8")
        # return self.unpad(cipher.decrypt(encoded_password[AES.block_size:])).decode('utf-8')


