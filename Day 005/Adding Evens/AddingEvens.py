# The program is going to write the sum of all even numbers
# Note: The solution should only be 1 statement


def main():
    max = input("Until what number shall all even numbers be added up? ")
    n = int(max) + 1
    sum = 0
    for i in range(0, n, 2):
        sum += i
    print(f"The sum is: {sum}")


main()
