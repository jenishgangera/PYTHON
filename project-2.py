print("Welcome to the Pattern Generator and Number Analyzer!")

while True:
    print("\nSelect an option:")
    print("1. Right-angled Triangle")
    print("2. Pyramid")
    print("3. Left-angled Triangle")
    print("4. Analyze a Range of Numbers")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # Right-angled Triangle
    if choice == "1":
        rows = int(input("Enter the number of rows for the pattern: "))

        if rows <= 0:
            print("Please enter a positive number.")
            continue

        print("\nPattern:")
        for i in range(1, rows + 1):
            for j in range(i):
                print("*", end="")
            print()

    # Pyramid
    elif choice == "2":
        rows = int(input("Enter the number of rows for the pattern: "))

        if rows <= 0:
            print("Please enter a positive number.")
            continue

        print("\nPattern:")
        for i in range(1, rows + 1):
            for j in range(rows - i):
                print(" ", end="")
            for j in range(2 * i - 1):
                print("*", end="")
            print()

    # Left-angled Triangle
    elif choice == "3":
        rows = int(input("Enter the number of rows for the pattern: "))

        if rows <= 0:
            print("Please enter a positive number.")
            continue

        print("\nPattern:")
        for i in range(1, rows + 1):
            for j in range(rows - i):
                print(" ", end="")
            for j in range(i):
                print("*", end="")
            print()

    # Number Analyzer
    elif choice == "4":
        start = int(input("Enter the start of the range: "))
        end = int(input("Enter the end of the range: "))

        if end <= start:
            print("End number must be greater than start number.")
            continue

        print("\nNumber Analysis:")

        even_numbers = []
        odd_numbers = []
        total = 0

        for number in range(start, end + 1):

            if number % 2 == 0:
                print("Number", number, "is Even")
                even_numbers.append(number)
            else:
                print("Number", number, "is Odd")
                odd_numbers.append(number)

            total += number

        print("\nEven Numbers:", even_numbers)
        print("Odd Numbers:", odd_numbers)
        print("Sum of all numbers:", total)

    # Exit
    elif choice == "5":
        print("Thank you for using the Pattern Generator and Number Analyzer!")
        break

    else:
        print("Invalid choice. Please select 1 to 5.")