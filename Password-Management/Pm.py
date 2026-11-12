
passwords = []

while True:
    print("\n====== Password Manager ======")
    print("1. Add Password")
    print("2. View Passwords")
    print("3. Search Password")
    print("4. Delete Password")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        website = input("Enter website name: ")
        username = input("Enter username: ")
        password = input("Enter demo password: ")

        details = {
            "website": website,
            "username": username,
            "password": password
        }

        passwords.append(details)
        print("Password added successfully!")

    elif choice == "2":
        if len(passwords) == 0:
            print("No passwords saved.")

        else:
            print("\nSaved Accounts:")

            for account in passwords:
                print("----------------------")
                print("Website:", account["website"])
                print("Username:", account["username"])
                print("Password:", account["password"])

    elif choice == "3":
        search = input("Enter website name: ")
        found = False

        for account in passwords:
            if account["website"].lower() == search.lower():
                print("Website:", account["website"])
                print("Username:", account["username"])
                print("Password:", account["password"])
                found = True

        if found == False:
            print("Account not found.")

    elif choice == "4":
        website = input("Enter website to delete: ")
        found = False

        for account in passwords:
            if account["website"].lower() == website.lower():
                passwords.remove(account)
                print("Account deleted successfully!")
                found = True
                break

        if found == False:
            print("Account not found.")

    elif choice == "5":
        print("Thank you for using Password Manager!")
        break

    else:
        print("Invalid choice! Please try again.")
