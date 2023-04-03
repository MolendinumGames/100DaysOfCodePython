# input: a whole number n
# output: either 'The number is odd' if n is an odd number
# or 'The number is even' if n is even

def main():
    number_input = input("Please type in a number: ")
    n = int(number_input)
    odd_message = "The number is odd."
    even_message = "The number is even."
    if n % 2 == 0:
        print(even_message)
    else:
        print(odd_message)


main()
