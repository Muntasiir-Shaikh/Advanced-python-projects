
expenses = []

while True:
    print("\n====== Expense Tracker ======")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expenses")
    print("4. Search by Category")
    print("5. Delete Expense")
    print("6. Exit")

    n = int(input("Enter your choice: "))

    if n == 1:
        name = input("Enter expense name: ")
        category = input("Enter category: ")

        try:
            amount = float(input("Enter amount: "))

            if amount <= 0:
                print("Enter a valid amount!")
                continue

            expense = {
                "name": name,
                "category": category,
                "amount": amount
            }

            expenses.append(expense)
            print("Expense added successfully!")

        except ValueError:
            print("Please enter a valid number.")

    elif n == 2:
        if len(expenses) == 0:
            print("No expenses found.")

        else:
            print("\nYour Expenses:")

            for i, expense in enumerate(expenses, start=1):
                print("--------------------")
                print("No:", i)
                print("Name:", expense["name"])
                print("Category:", expense["category"])
                print("Amount: ₹", expense["amount"])

    elif n == 3:
        total = 0

        for expense in expenses:
            total += expense["amount"]

        print("Total Expenses: ₹", total)

    elif n == 4:
        category = input("Enter category to search: ")
        found = False

        for expense in expenses:
            if expense["category"].lower() == category.lower():
                print("--------------------")
                print("Name:", expense["name"])
                print("Amount: ₹", expense["amount"])
                found = True

        if found == False:
            print("No expenses found in this category.")

    elif n == 5:
        if len(expenses) == 0:
            print("No expenses to delete.")

        else:
            for i, expense in enumerate(expenses, start=1):
                print(i, ".", expense["name"], "-", expense["amount"])

            try:
                number = int(input("Enter expense number to delete: "))

                if 1 <= number <= len(expenses):
                    expenses.pop(number - 1)
                    print("Expense deleted successfully!")
                else:
                    print("Invalid expense number.")

            except ValueError:
                print("Please enter a valid number.")

    elif n == 6:
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice! Try again.")
