from Shared import save_contact, display_contact, edit_contact, delete_contact


def main():
    
    print("""
        Welcome to the Contact Book saver:

        1. Save Contact
        2. Display Contacts
        3. Edit Contacts
        4. Delete Contacts
        5. Exit  
        """)

    choice = int(input('> '))

    if choice == 1:
        save_contact()

    if choice == 2:
        display_contact()

    if choice == 3:
        edit_contact()

    if choice == 4:
        delete_contact()

    if choice == 5:
        pass


main()