# Task: Create a tip calculator
# ask for the amount of the bill, the percentage of the tip and
# how many people will split the bill

def main():
    print("Welcome to the tip calculator!")
    bill_input = input("Please enter the amount of the bill: ")
    perc_input = input("Please enter the percentage of the tip? (10, 12, 15?): ")
    people_input = input("Please enter how many people will split the bill: ")
    bill = float(bill_input)
    tip_perc = int(perc_input)
    people = int(people_input)

    tip_mult = (tip_perc + 100) / 100
    total_bill = bill * tip_mult
    indv_amount = round(total_bill / people, 2)
    formatted_indv_amount = "{:.2f}".format(indv_amount)

    message = f"Each person will have to pay {formatted_indv_amount}€"
    print(message)


main()
