# div by 3 = fizz
# div by 5 = buzz
# div by both = fizzbuzz

START = 1


def play(n: int):
    for i in range(START, n + 1):
        text = ""
        if i % 3 == 0:
            text += "Fizz"
        if i % 5 == 0:
            text += "Buzz"
        if text == "":
            text = str(i)
        print(text)


def main():
    count_to = 100
    play(count_to)


main()
