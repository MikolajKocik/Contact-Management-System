Contact Management System
Overview

This project is a simple Contact Management System written in Python. It allows users to add, search, edit, delete, and view contacts. Contacts are stored in a JSON file for persistence between program runs.
Features

    Add Contact: Allows the user to add a new contact with a name and number.
    Search Contact: Allows the user to search for contacts by name.
    View All Contacts: Displays all the contacts.
    Delete Contact: Allows the user to delete a contact by name.
    Edit Contact: Allows the user to edit the name or number of an existing contact.
    Save Contacts: Contacts are automatically saved to a JSON file when the program closes.

Technical Details

    Type Hinting: The project uses Python's type hinting to improve code readability and provide hints about what types of arguments and return values functions expect.
    JSON Serialization: Contacts are stored in a JSON file to ensure data persistence. The Contact class includes methods to convert instances to and from dictionaries, making JSON serialization straightforward.
    List Comprehension: The project uses list comprehensions for concise and readable operations on lists, such as searching for contacts.
    Regular Expressions (Regex): The project uses regular expressions to validate user input, ensuring that names contain only valid characters and phone numbers follow the required format.
