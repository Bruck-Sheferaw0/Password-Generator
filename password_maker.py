from password_data import letters, numbers, symbols
import random


class PasswordGenerator:
    def __init__(self, user_letters, user_numbers, user_symbols):
        self.letters = user_letters
        self.numbers = user_numbers
        self.symbols = user_symbols
        self.total_password = []

    def letters_maker(self):
        for i in range(0,self.letters):
            self.total_password.append(random.choice(letters))

    def numbers_maker(self):
        for i in range(0,self.numbers):
            self.total_password.append(random.choice(numbers))

    def symbols_maker(self):
        for i in range(0,self.symbols):
            self.total_password.append(random.choice(symbols))
            random.shuffle(self.total_password)
        print(f"Here is you random password: {"".join(self.total_password)}")
