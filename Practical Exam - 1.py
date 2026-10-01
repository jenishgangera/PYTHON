print("Welcome to the Bill Splitter App!")

while True:

    # User Inputs
    people = int(input("\nEnter number of people: "))
    bill = float(input("Enter total bill amount: "))
    tip = int(input("Enter tip percentage (0/5/10/15/20): "))

    # Validation
    if people <= 0:
        print("Error: Number of people must be greater than 0.")
        continue

    if bill < 0:
        print("Error: Bill amount cannot be negative.")
        continue

    if tip not in [0, 5, 10, 15, 20]:
        print("Error: Tip percentage must be 0, 5, 10, 15, or 20.")
        continue

    # Calculations
    tip_amount = (tip / 100) * bill
    total_bill = bill + tip_amount
    per_person = total_bill / people

    # Output
    print("\n----- Bill Summary -----")
    print(f"Tip Amount: ₹{tip_amount:.2f}")
    print(f"Total Bill (with Tip): ₹{total_bill:.2f}")
    print(f"Each Person Should Pay: ₹{per_person:.2f}")

    # Repeat
    again = input("\nWould you like to calculate another bill? (y/n): ")

    if again.lower() != "y":
        print("\nThank you for using the Bill Splitter App!")
        break
       