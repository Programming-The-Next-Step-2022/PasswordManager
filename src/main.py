import src.PasswordManager
import src.Encryption

if __name__ == '__main__':
    password_manager = src.PasswordManager.PasswordManager()
    password_manager.init_input()
    print(password_manager.find_password('google'))

    message = input("Enter message to encrypt: ");
    key = input("Enter encryption key: ")
    encrypted_msg = encrypt(message, key)
    print("Encrypted Message:", encrypted_msg)
    decrypted_msg = decrypt(encrypted_msg, key)
    print("Decrypted Message:", bytes.decode(decrypted_msg))
