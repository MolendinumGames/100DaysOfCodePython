import random

ROCK_ART = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

PAPER_ART = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

SCISSOR_ART = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""


def draw(choice: chr):
    if choice == "r":
        print(ROCK_ART)
    elif choice == "p":
        print(PAPER_ART)
    else:
        print(SCISSOR_ART)


def main():
    user_choice = (input('Type R for Rock, P for Paper or S for Scissors: ').lower())
    draw(user_choice)
    ai_choice = random.choice(["r", "p", 's'])
    print("I chose:")
    draw(ai_choice)
    if ai_choice == user_choice:
        print("It's a draw!")
    elif ai_choice == "r":
        if user_choice == "p":
            print("You win!")
        else:
            print("I win!")
    elif ai_choice == "p":
        if user_choice == "r":
            print("You win!")
        else:
            print("I win!")
    else:  # ai_choice == s
        if user_choice == "p":
            print("I win!")
        else:
            print("You win!")


main()
