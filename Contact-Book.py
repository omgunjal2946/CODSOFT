contacts = {}

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contacts[name] = {"Phone": phone, "Email": email, "Address": address}
    print("Contact added successfully.")

def view_contacts():
    if not contacts:
        print("No contacts to display.")
        return
    for name, details in contacts.items():
        print(f"\nName: {name}")
        for key, value in details.items():
            print(f"{key}: {value}")

def search_contact():
    search = input("Enter name or phone to search: ")
    for name, details in contacts.items():
        if search == name or search == details["Phone"]:
            print(f"\nFound Contact:\nName: {name}")
            for key, value in details.items():
                print(f"{key}: {value}")
            return
    print("Contact not found.")

def update_contact():
    name = input("Enter name to update: ")
    if name in contacts:
        print("Leave blank if no change.")
        phone = input("New phone: ") or contacts[name]["Phone"]
        email = input("New email: ") or contacts[name]["Email"]
        address = input("New address: ") or contacts[name]["Address"]
        contacts[name] = {"Phone": phone, "Email": email, "Address": address}
        print("Contact updated.")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter name to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted.")
    else:
        print("Contact not found.")

while True:
    print("\n--- Contact Book Menu ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        update_contact()
    elif choice == '5':
        delete_contact()
    elif choice == '6':
        print("Exiting Contact Book. Goodbye!")
        break
    else:
        print("Invalid choice, try again.")
