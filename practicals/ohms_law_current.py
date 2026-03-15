# Beginner-friendly Ohm's Law calculator with input checks
print("Ohm's Law (I = V / R)")
print("This program calculates current and tells you if it is low, normal, or high.")

def read_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

voltage = read_float("Enter voltage in volts (V): ")
resistance = read_float("Enter resistance in ohms (O): ")

if resistance == 0:
    print("Resistance cannot be zero. Please run the program again.")
else:
    current = voltage / resistance
    print("Current I is:", round(current, 3), "A")

    if current < 0.5:
        print("Low current")
    elif current <= 2:
        print("Normal current")
    else:
        print("High current")
