# Employee salary calculator
print("Employee Salary Information Generator")
name = input("Enter employee name: ")
employee_id = input("Enter employee ID: ")
department = input("Enter department: ")

while True:
    try:
        basic = float(input("Enter basic salary (Rs): "))
        if basic < 0:
            print("Basic salary must be non-negative. Try again.")
            continue
        break
    except ValueError:
        print("Please enter a valid number.")

# Salary components
DA = 0.92 * basic
HRA = 0.58 * basic
TA = 0.30 * basic
LIC = 500.0

gross_salary = basic + DA + HRA + TA
net_salary = gross_salary - LIC

print("\n--- Employee Salary Details ---")
print(f"Name       : {name}")
print(f"Employee ID: {employee_id}")
print(f"Department : {department}")
print(f"Basic      : Rs {basic:,.2f}")
print(f"DA (92%)   : Rs {DA:,.2f}")
print(f"HRA (58%)  : Rs {HRA:,.2f}")
print(f"TA (30%)   : Rs {TA:,.2f}")
print(f"LIC Deduct : Rs {LIC:,.2f}")
print(f"Gross Sal  : Rs {gross_salary:,.2f}")
print(f"Net Salary : Rs {net_salary:,.2f}")
