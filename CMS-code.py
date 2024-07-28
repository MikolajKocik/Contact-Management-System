import re # regex
import json
from typing import List, Optional # hint types

class Contact:

    def __init__(self, number: str, name: str) -> None: 
        # example of hint type parameter: type / -> type(what returns)
        self.number = number
        self.name = name
    # Initialize a Contact object with a number and name.    

    def __repr__(self) -> str:
        return f"Contact(name={self.name}, number={self.number})"
    """
        Return a string representation of the Contact object.
        Useful for debugging and logging.
    """

    def to_dict(self) -> dict:
        return {"number": self.number, "name": self.name}
    """
        Convert the Contact object to a dictionary.
        Useful for serialization.
    """

    @classmethod
    def from_dict(cls, data: dict) -> 'Contact':
        return cls(data["number"], data["name"])
    """
        Create a Contact object from a dictionary.
        Useful for deserialization.
    """

def save_contacts(contacts: List[Contact], filename: str = 'contacts.json') -> None:
    with open(filename, 'w') as file:
        json.dump([contact.to_dict() for contact in contacts], file, indent=4)
        # Convert each Contact to a dictionary and write the list to a JSON file

def load_contacts(filename: str = 'contacts.json') -> List[Contact]:
    try:
        with open(filename, 'r') as file:
            contacts_data = json.load(file)
            # Convert each dictionary back to a Contact object
            return [Contact.from_dict(data) for data in contacts_data]
    except FileNotFoundError:
        return []

def add_contact(contacts: List[Contact]) -> None:
    while True:
        try:
            name = input("Write a name: ")
            if re.match(r"^[A-Za-zą-źżńśóŁŚĆŹŻŃŚÓ]+(\s[A-Za-zą-źżńśóŁŚĆŹŻŃŚÓ]+)*$", name):
                break
            else:
                raise ValueError("Invalid name format. Please try again.")
        except ValueError as e:
            print("Value error: ", e)

    while True:
        try:
            number = input("Write a number (must contain 9 numerals): ")
            if re.match(r"^\d{9}$", number):
                break
            else:
                raise ValueError("Invalid number format. Please try again.")
        except ValueError as e:
            print("Value error: ", e)

    new_contact = Contact(number, name)
    contacts.append(new_contact)
    print(f"New contact: {name} : {number}")

def search_contacts(contacts: List[Contact]) -> None:
    name = input("Enter the name to search: ")
    # list comprehesion
    found_contacts = [contact for contact in contacts if name.lower() in contact.name.lower()]
    if found_contacts:
        for contact in found_contacts:
            print(f"Name: {contact.name}, Number: {contact.number}")
    else:
        print("No contacts found with that name.")

def search_all_contacts(contacts: List[Contact]) -> None:
    if not contacts:
        print("No contacts available.")
        return
    print("\nList of all contacts:")
    for contact in contacts:
        print(f"Name: {contact.name}, Number: {contact.number}")

def delete_contact(contacts: List[Contact]) -> None:
    name = input("Enter the name of the contact to delete: ")
    contact_to_delete: Optional[Contact] = None
    for contact in contacts:
        if contact.name.lower() == name.lower():
            contact_to_delete = contact
            break
    if contact_to_delete:
        contacts.remove(contact_to_delete)
        print(f"Contact {name} deleted.")
    else:
        print("Contact not found.")

def edit_contact(contacts: List[Contact]) -> None:
    name = input("Enter the name of the contact to edit: ")
    contact_to_edit: Optional[Contact] = None
    for contact in contacts:
        if contact.name.lower() == name.lower():
            contact_to_edit = contact
            break
    if contact_to_edit:
        new_name = input(f"Enter new name (leave blank to keep '{contact_to_edit.name}'): ")
        new_number = input(f"Enter new number (leave blank to keep '{contact_to_edit.number}'): ")
        if new_name:
            contact_to_edit.name = new_name
        if new_number:
            contact_to_edit.number = new_number
        print(f"Contact {name} updated.")
    else:
        print("Contact not found.")

def main_menu() -> None:
    contacts = load_contacts()
    while True:
        print("\nMenu:")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Search All Contacts")
        print("4. Delete Contact")
        print("5. Edit Contact")
        print("6. Close Program")
        choice = input("Choose an option (1-6): ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            search_contacts(contacts)
        elif choice == '3':
            search_all_contacts(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            edit_contact(contacts)
        elif choice == '6':
            save_contacts(contacts)
            print("Contacts have been saved. Closing program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
