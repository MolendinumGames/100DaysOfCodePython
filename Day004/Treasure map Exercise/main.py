# The program should take 2 digits and mark the hiding spot
# of the treasure on a 3x3 field. The two input numbers
# need to be entered like this: "1 2"

def main():
    row1 = ['░', '░', '░']
    row2 = ['░', '░', '░']
    row3 = ['░', '░', '░']
    field = [row1, row2, row3]

    position = input('Where do you want your treasure to be hidden? ')

    # get the int value from the entered position.
    # We have to deduct 1 since our index start at 0
    x_coord = int(position.split(' ')[0]) - 1
    y_coord = int(position.split(' ')[1]) - 1

    # Mark the treasure spot:
    field[x_coord][y_coord] = 'X'

    #print the result:
    print("The treasure is hidden at:")
    print(f"{row1}\n{row2}\n{row3}")


main()
