name = "Hu Cheng Wei"
age = 22
height = 1.78
is_student = True

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is student:", is_student)

print("\n--- Type Conversion ---")
print(int(4.7)) 
print(float(1))
print(str(True))
print(bool(5))
print(bool(0))

print("\n--- String Formatting ---")
people = 4
time = "7pm"
print("We would like to reserve a table for {} at {}".format(people, time))
print(f"We would like to reserve a table for {people} at {time}")