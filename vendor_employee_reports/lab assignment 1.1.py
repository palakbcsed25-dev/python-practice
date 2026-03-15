# Beginner-friendly Vendor annual purchase billing report with safe input
print("Vendor Purchase/Billing Report")

name = input("Enter vendor name: ")
year = input("Enter year of association: ")
contact = input("Enter contact number: ")
email = input("Enter email ID: ")


def get_amount(month):
    while True:
        t = input(f"{month}: ")
        if t.strip() == "":
            return 0.0
        try:
            return float(t)
        except ValueError:
            print("Please enter a number (or leave blank for 0).")

print("\nEnter monthly purchase amounts (in Rs):")
jan = get_amount("January")
feb = get_amount("February")
mar = get_amount("March")
apr = get_amount("April")
may = get_amount("May")
jun = get_amount("June")
jul = get_amount("July")
aug = get_amount("August")
sep = get_amount("September")
oct = get_amount("October")
nov = get_amount("November")
dec = get_amount("December")

annual_total = jan + feb + mar + apr + may + jun + jul + aug + sep + oct + nov + dec
average = annual_total / 12

print("\n--- Annual Vendor Purchase Report ---")
print("Vendor Name         :", name)
print("Year of Association :", year)
print("Contact Number      :", contact)
print("Email ID            :", email)
print("Total Annual Purchase : Rs", annual_total)
print("Average Monthly Purchase : Rs", round(average, 2))
