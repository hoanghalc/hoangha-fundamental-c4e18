height_cm = int(input("How are your height:"))
weight = int(input("How are your weight:"))
height = float(height_cm/100)
bmi = float(weight/(height*height))

if bmi < 16:
    print("Severely underweight")
elif bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal")
elif bmi <= 30:
    print("Overweight")
else:
    print("Obese")


