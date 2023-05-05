import random


def main():
    word_list = ["ardvark", "baboon", "camel"]
    solution = random.choice(word_list)
    word_length = len(solution)
    display = []
    for i in range(word_length):
        display.append('_')

    while not display.__contains__('_'):
        guess = input("Please guess a letter: ").lower()
        for i in range(word_length):
            if guess == solution[i]:
                display[i] = solution[i]
        print(display)


main()
