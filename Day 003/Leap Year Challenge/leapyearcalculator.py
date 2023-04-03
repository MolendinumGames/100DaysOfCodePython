# input: a year as integer
# output: Is a leap year or not a leap year
# A year is a leap year if it is:
# evenly divisible by 4
#   except evenly divisible by 100
#       unless also divisible by 400

def main():
    number_input = input("Please type in a year: ")
    n = int(number_input)

    is_leap = False
    if n % 4 == 0:
        if n % 100 == 0:
            if n % 400 == 0:
                is_leap = True
            else:
                is_leap = False
        else:
            is_leap = True
    else:
        is_leap = False

    if is_leap:
        print(f"The year {n} is a leap year.")
    else:
        print(f"The year {n} is not a leap year.")


main()
