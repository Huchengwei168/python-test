score = int(input("Please enter your score: "))

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

print(f"Your score is {score}.")

print("\n--- BMI Calculator ---")
weight = float(input("Enter weight (kg): "))
height = float(input("Enter height (m): "))
bmi = weight / (height ** 2)

if bmi >= 25:
    print("Overweight")
elif bmi < 18.5:
    print("Underweight")
else:
    print("Normal")
print(f"Your BMI is {bmi:.2f}")