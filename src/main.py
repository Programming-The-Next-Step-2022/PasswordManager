import src.test

if __name__ == '__main__':
    password_manager = src.test.PasswordManager()
    password_manager.init_input()
    print(password_manager.find_password('google'))


