contacts = {}

while True:
    print("\n---CONTACT BOOK---")
    print("1. Add contact")
    print("2. View all contacts")
    print("3. Search Contact")
    print("4. Delete contact")
    print("5.exit")

    choice = input("Enter your decision:")

    if choice == "1":
        name = input("Enter contact name:")
        phone = input("Enter phone number:")
        contacts[name] =phone
        print("Contact added!")

    elif choice == "2":
        print("\nAll contacts:")
        if len(contacts)==0:
            print("No contats saved yet.")
        else:
            for name, phone in contacts.items():
                print(name, "-", phone)

    elif choice == "3":
        name = input("Enter name to search:")
        if name in contacts:
            print(name, "-", contacts[name])
        else:
            print("Contact not found")

    elif choice == "4":
        name = input("Enter name to delete:")
        if name in contacts:
            del contacts[name]
            print("Contact deleted!")
        else:
            print("Contact not found")
    elif  choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try later")

