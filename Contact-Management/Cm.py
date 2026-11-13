
contacts = []

while True:
    print("\n====== Contact Management System ======")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")

        contact = {
            "name": name,
            "phone": phone,
            "email": email
        }

        contacts.append(contact)
        print("Contact added successfully!")

    elif choice == "2":
        if len(contacts) == 0:
            print("No contacts found.")

        else:
            print("\nYour Contacts:")

            for i, contact in enumerate(contacts, start=1):
                print("--------------------")
                print("Contact No:", i)
                print("Name:", contact["name"])
                print("Phone:", contact["phone"])
                print("Email:", contact["email"])

    elif choice == "3":
        search_name = input("Enter name to search: ")
        found = False

        for contact in contacts:
            if contact["name"].lower() == search_name.lower():
                print("\nContact Found!")
                print("Name:", contact["name"])
                print("Phone:", contact["phone"])
                print("Email:", contact["email"])
                found = True

        if found == False:
            print("Contact not found.")

    elif choice == "4":
        name = input("Enter contact name to update: ")
        found = False

        for contact in contacts:
            if contact["name"].lower() == name.lower():
                contact["phone"] = input("Enter new phone number: ")
                contact["email"] = input("Enter new email: ")

                print("Contact updated successfully!")
                found = True
                break

        if found == False:
            print("Contact not found.")

    elif choice == "5":
        name = input("Enter contact name to delete: ")
        found = False

        for contact in contacts:
            if contact["name"].lower() == name.lower():
                contacts.remove(contact)
                print("Contact deleted successfully!")
                found = True
                break

        if found == False:
            print("Contact not found.")

    elif choice == "6":
        print("Thank you for using Contact Management System!")
        break

    else:
        print("Invalid choice! Try again.")
