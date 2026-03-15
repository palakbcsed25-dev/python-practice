# Beginner-friendly Steel Grade Calculator
print("Steel Grade Calculator")
print("Enter the following steel test values:")

def input_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

hardness = input_float("Hardness value: ")
carbon = input_float("Carbon content: ")
tensile = input_float("Tensile strength: ")

condition1 = hardness > 50
condition2 = carbon < 0.7
condition3 = tensile > 5600

if condition1 and condition2 and condition3:
    grade = 10
elif condition1 and condition2:
    grade = 9
elif condition2 and condition3:
    grade = 8
elif condition1 and condition3:
    grade = 7
elif condition1 or condition2 or condition3:
    grade = 6
else:
    grade = 5

print("\nResults:")
print("Hardness > 50?", condition1)
print("Carbon < 0.7?", condition2)
print("Tensile strength > 5600?", condition3)
print("Final steel grade:", grade)
