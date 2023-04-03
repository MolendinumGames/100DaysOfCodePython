# BMI = weight (kg) / height(m)^2

def main():
    weight = input("Please enter your weight in kg: ")
    height = input("Please enter your height in m: ")

    bmi = int(weight) / float(height) ** 2
    print("Your BMI is: " + str(int(bmi)))


main()
