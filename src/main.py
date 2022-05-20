import src.PasswordManager

if __name__ == '__main__':
    password_manager = src.PasswordManager.PasswordManager()
    password_manager.init_input()
    print(password_manager.find_password('google'))
