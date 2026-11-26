
print("Welcome to Pattern Generator and Number Analyzer!")

while True:
    print("\n1. Pattern Generation")
    print("2. Number Analysis")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        rows = int(input("Enter number of rows: "))

        if rows <= 0:
            print("Invalid number of rows!")
            continue

        for i in range(1, rows + 1):
            for j in range(i):
                print("*", end=" ")
            print()

    elif choice == "2":
        start = int(input("Enter starting number: "))
        end = int(input("Enter ending number: "))

        if start > end:
            print("Invalid range!")
            continue

        total = 0

        print("Odd numbers:")
        for i in range(start, end + 1):
            if i % 2 == 0:
                continue
            print(i, end=" ")

        print("\nEven numbers:")
        for i in range(start, end + 1):
            if i % 2 != 0:
                continue
            print(i, end=" ")

        for i in range(start, end + 1):
            total = total + i

        print("\nSum of all numbers:", total)

    elif choice == "3":
        print("Thank you for using the program!")
        break

    else:
        print("Invalid choice! Please try again.")
        pass