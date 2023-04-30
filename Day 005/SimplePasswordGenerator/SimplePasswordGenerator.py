import random

SYMBOLS = ['.', ':', ',', ';', '#', '+', '-', '(', ')', '&', '$', '!', '?', '%']


def get_letter():
    letter = chr(random.randint(65, 90))
    return random.choice([letter, letter.lower()])


def get_symbol():
    return random.choice(SYMBOLS)


def get_number():
    return str(random.randint(0, 9))


def main():
    password_list = []
    numbers_count = int(input("How many digits should the password have? "))
    letter_count = int(input("How many letters should the password have? "))
    symbol_count = int(input("How many symbols should the password have? "))
    for i in range(0, numbers_count):
        password_list.append(get_number())
    for i in range(0, letter_count):
        password_list.append(get_letter())
    for i in range(0, symbol_count):
        password_list.append(get_symbol())
    random.shuffle(password_list)
    password = ""
    for i in range(0, len(password_list) - 1):
        password += password_list[i]
    print(password)


main()

