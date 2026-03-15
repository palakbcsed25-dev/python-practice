# Bank Account Menu Driven Program

balance = 0

def display_balance():
    print("Current Balance:", balance)

def deposit(amount):
    global balance
    balance = balance + amount
    print("Amount Deposited Successfully")

def withdraw(amount):
    global balance
    if amount > balance:
        print("Insufficient Balance")
    else:
        balance = balance - amount
        print("Amount Withdrawn Successfully")


while True:
    print("\n----- BANK MENU -----")
    print("1. Display Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        display_balance()

    elif choice == 2:
        amount = float(input("Enter amount to deposit: "))
        deposit(amount)

    elif choice == 3:
        amount = float(input("Enter amount to withdraw: "))
        withdraw(amount)

    elif choice == 4:
        print("Thank you for using the Bank System")
        break

    else:
        print("Invalid Choice")