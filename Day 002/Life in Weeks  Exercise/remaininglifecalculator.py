
def main():
    # given
    age_input = input("Enter your current age: ")

    # print out the remaining total days, total weeks, total months and total years left if the expected
    # max age of a person is 90. Disregarding the progress within the current year of the life and
    # leap years
    age = int(age_input)
    remaining_years = 90 - age
    remaining_months = remaining_years * 12
    remaining_weeks = remaining_years * 52
    remaining_days = remaining_years * 365

    print(f"If the person would live to 90, they would have about {remaining_years} years " +
          f"remaining or {remaining_months} months or {remaining_weeks} weeks or {remaining_days} days.")


main()
