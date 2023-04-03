# task: Switch the value of the 2 variables a and b
def main():
    # Given:
    a = input('a: ')
    b = input('b: ')

    # Solution:
    temp_a = a
    a = b
    b = temp_a
    print('a: ' + str(a))
    print('b: ' + str(b))


main()