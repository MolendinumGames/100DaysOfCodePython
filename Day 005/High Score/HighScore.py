# Lets the user input a list of scores separated by comma
# and then prints out the highest score
# The task was to solve the problem using a for loop instead of
# using the max/min function


def main():
    all_scores = input("Please enter all scores separated by a space: ").split()
    highscore = 0
    for i in range(0, len(all_scores)):
        current_score = int(all_scores[i])
        if current_score > highscore:
            highscore = current_score
    print(f"The highest score is: {highscore}")


main()
