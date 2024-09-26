def BMI(weight, height):

    bmi = (weight/(height**2))
    bmi_str = str(round(bmi, 2))

    weight_status = ""
    if bmi < 18.5:
        weight_status = "Underweight"
    elif 24.9 >= bmi >= 18.5:
        weight_status = "Normal Weight"
    elif 25<= bmi <= 29.9:
        weight_status = "Overweight"
    elif bmi >= 30:
        weight_status = "Obesity"
    else :
        print("Something is Wrong.")

    print("Your BMI is " + bmi_str + ". You are classified as " + weight_status + ".")
    print(f"Your BMI is {bmi_str}. You are classified as {weight_status}.")


your_weight = float(input("Enter your weight in kilograms: "))
your_height = float(input("Enter your height in meters: "))

BMI(your_weight, your_height)