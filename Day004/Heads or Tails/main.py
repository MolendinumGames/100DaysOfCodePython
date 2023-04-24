import random

def main():
    rnd_num = random.randint(0, 1)
    action = ""
    if rnd_num == 0:
        action = "Heads"
    else:
        action = "Tails"
    print(f"The coin shows {action}")


main()
