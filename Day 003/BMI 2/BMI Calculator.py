# BMI = weight (kg) / height(m)^2

def main():
    # Updated code from BMI Day002
    weight_input = input("Please enter your weight in kg: ")
    height_input = input("Please enter your height in m: ")
    weight = int(weight_input)
    height = float(height_input)

    bmi = weight / height ** 2
    print("Your BMI is: " + str(round(bmi)))

    # BMI 2.0 Day003
    bmi_msg = ""
    if bmi > 35:
        bmi_msg = "clinically obese"
    elif bmi > 30:
        bmi_msg = "obese"
    elif bmi > 25:
        bmi_msg = "overweight"
    elif bmi > 18.5:
        bmi_msg = "normal weight"
    else:
        bmi_msg = "underweight"

    print(f"The interpretation of your BMI is: {bmi_msg}")


main()
