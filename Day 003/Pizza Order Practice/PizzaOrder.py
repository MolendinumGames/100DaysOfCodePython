# Based on a users order, work out their final bill
# Small Pizza $15, medium $20, large $25
# Pepperoni for small pizza $2, for med and large $3
# extra cheese for any size: $1
# Inputs in S, M, L for sizes and Y/N for extras

def main():
    print("Welcome to Python Pizza Deliveries!")
    size_input = input("What size of pizza do you want? S, M or L: ")
    pepperoni_input = input("Do you want to add extra pepperoni (Y/N)? ")
    cheese_input = input("Do you want to add extra cheese (Y/N)? ")

    bill = 0

    if size_input == "S":
        bill += 15
    elif size_input == "M":
        bill += 20
    else: #L
        bill += 25

    if pepperoni_input == "Y":
        if size_input == "S":
            bill += 2
        else: #M/L
            bill += 3

    if cheese_input == "Y":
        bill += 1

    bill_formatted = "{:.2f}".format(bill)
    print(f"Your final bill is: ${bill_formatted}")


main()
