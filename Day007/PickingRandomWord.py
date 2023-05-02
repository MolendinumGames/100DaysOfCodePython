import random


def main():
    word_list = ["ardvark", "baboon", "camel"]
    solution = random.choice(word_list)
    display = []
    for i in range(0, len(solution)):
        display.append('_')
    while display.__contains__('_'):
        guess = input("Please guess a letter: ").lower()
        for i in range(0, len(solution)):
            if guess == solution[i]:
                display[i] = solution[i]
        print(display)


main()
