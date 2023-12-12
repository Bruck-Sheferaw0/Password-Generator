from password_maker import PasswordGenerator

user_letters = int(input("How many letters do you want? "))
user_numbers = int(input("How many numbers do you want? "))
user_symbols = int(input("How many symbols do you want? "))

user_password = PasswordGenerator(user_letters, user_numbers, user_symbols)
user_password.letters_maker()
user_password.numbers_maker()
user_password.symbols_maker()

