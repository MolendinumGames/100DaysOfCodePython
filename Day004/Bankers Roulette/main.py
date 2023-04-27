# Prompts the user to enter a list of names and prints
# a randomly selected name from the list as chosen person
# to pay the bill. Based on the game 'bankers roulette'
# from: 100 days of code day 4 challenge 2

import random


def main():
    names_input = input('Please enter all participants separated by comma: ')
    names = names_input.split(', ')

    rnd = random.randint(0, len(names) - 1)
    # alternatively we can use:
    # random_name = random.choice(names)

    print(f"{names[rnd]} was randomly selected to pay the bill!")


main()
