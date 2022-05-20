import base64
import hashlib
from Crypto.Cipher import AES
from Crypto import Random


class Encryption(object):

    def __init__(self, key):
        self.key = hashlib.sha256(key.encode()).digest()
        self.blocksize = AES.block_size

    def pad(self, s):
        return s + (self.blocksize - len(s) % self.blocksize) * chr(
            self.blocksize - len(s) % self.blocksize)

    def unpad(self, s):
        return s[:-ord(s[len(s) - 1:])]

    def encrypt(self, password):
        padded_password = self.pad(password)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(padded_password.encode()))

    def decrypt(self, encoded_password):
        encoded_password = base64.b64decode(encoded_password)
        iv = encoded_password[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        # return self.unpad(cipher.decrypt(encoded_password[self.bs:]))
        return self.unpad(cipher.decrypt(encoded_password[AES.block_size:])).decode('utf-8')


