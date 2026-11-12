
books = []

while True:
    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter book name: ")
        author = input("Enter author name: ")

        book = {
            "name": name,
            "author": author,
            "status": "Available"
        }

        books.append(book)
        print("Book added successfully!")

    elif choice == "2":
        if len(books) == 0:
            print("No books available.")

        else:
            print("\nLibrary Books:")

            for book in books:
                print("--------------------")
                print("Book:", book["name"])
                print("Author:", book["author"])
                print("Status:", book["status"])

    elif choice == "3":
        search = input("Enter book name: ")
        found = False

        for book in books:
            if book["name"].lower() == search.lower():
                print("Book:", book["name"])
                print("Author:", book["author"])
                print("Status:", book["status"])
                found = True

        if found == False:
            print("Book not found.")

    elif choice == "4":
        name = input("Enter book name to issue: ")
        found = False

        for book in books:
            if book["name"].lower() == name.lower():
                found = True

                if book["status"] == "Available":
                    book["status"] = "Issued"
                    print("Book issued successfully!")
                else:
                    print("Book is already issued.")

                break

        if found == False:
            print("Book not found.")

    elif choice == "5":
        name = input("Enter book name to return: ")
        found = False

        for book in books:
            if book["name"].lower() == name.lower():
                found = True

                if book["status"] == "Issued":
                    book["status"] = "Available"
                    print("Book returned successfully!")
                else:
                    print("This book was not issued.")

                break

        if found == False:
            print("Book not found.")

    elif choice == "6":
        print("Thank you for using Library Management System!")
        break

    else:
        print("Invalid choice! Try again.")
