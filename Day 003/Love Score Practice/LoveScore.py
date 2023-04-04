# input: 2 names
# output: a 2 digit score with an interpretation
# first digit is how many times  the letters t r u e appear in both names combined between 0 and 9
# second digit is how many times the letters l o v e appear in both names combined between 0 and 9
# if the score is less than 10 or more than 9 msg: "Your score is x, you go together like coke and mentos."
# if score is between 40 and 50: "Your score is x, you are alright together."
# otherwise just print: "your score is x."

def main():
    print("Welcome to the Love Calculator!")
    name1 = input("Please enter your name: ").lower()
    name2 = input("Please enter the name of the other person: ").lower()
    combined_names = name1 + name2

    first_digit = 0
    first_digit += combined_names.count("t")
    first_digit += combined_names.count("r")
    first_digit += combined_names.count("u")
    first_digit += combined_names.count("e")
    if first_digit > 9:
        first_digit = 9

    second_digit = 0
    second_digit += combined_names.count("l")
    second_digit += combined_names.count("o")
    second_digit += combined_names.count("v")
    second_digit += combined_names.count("e")
    if second_digit > 9:
        second_digit = 9

    final_score = int(str(first_digit)+str(second_digit))
    if final_score < 10 or final_score > 90:
        print(f"Your score is {final_score}, you go together like coke and mentos.")
    elif 40 < final_score < 50:
        print(f"Your score is {final_score}, you are alright together.")
    else:
        print(f"Your score is {final_score}")


main()
