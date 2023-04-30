# Lets the user input a list of student heights and
# then prints out the average student height
# The solution must incorporate a for loop


def main():
    student_heights = input('Enter a list of student heights: ').split(' ')
    sum = 0.0
    for h in student_heights:
        sum += float(h)
    avrg_height = sum / len(student_heights)
    print(f"The average student height is: {avrg_height:.1f}")


main()
