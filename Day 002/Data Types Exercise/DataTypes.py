# Instructions
# Write a program that adds the digits in a 2 digit number. e.g. if the
# input was 35, then the output should be 3 + 5 = 8
# Note: No extra functions, loops or input validation yet

def main():
    input_number = input("Enter a 2 digit number: ")
    sum_of_digits = int(input_number[0]) + int(input_number[1])
    print("The sum of the digits is: " + str(sum_of_digits))


main()
