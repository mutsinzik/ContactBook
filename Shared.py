from db import db,mycursor


# Function that saves contact in database
def save_contact():
    first_name = input("Please enter the first name: ")
    last_name = input("Please enter the last name: ")
    addy = input("Please enter the contact's address: ")
    phone_num = (input("Please enter the contact's phone number: "))
    
    save_query = "INSERT INTO contact_table VALUES(%s, %s, %s, %s)"
    val = (first_name, last_name, addy, phone_num)
    mycursor.execute(save_query,val)
    db.commit()
    print("Contact Saved successfully")
    
# Function to display contacts
def display_contact():
    display_query = "SELECT * FROM contact_table"
    mycursor.execute(display_query)
    
    print("First Name\t\t\tLast Name\t\t\tAddress\t\t\tPhone Number")
    print("----------\t\t\t---------\t\t\t-------\t\t\t------------")
    for first_name, last_name, address, phone_number in mycursor:
        print(f"{first_name}\t\t\t\t{last_name}\t\t\t{address}\t\t\t{phone_number}")
        
# Function to edit a contact      
def edit_contact():
    edit_contact = input("Enter name of contact you want to edit:")
    search_query = "SELECT fname FROM contact_table"
    mycursor.execute(search_query)
    
    if (edit_contact,) in mycursor:
        first_name = input("Please enter the first name: ")
        last_name = input("Please enter the last name: ")
        addy = input("Please enter the contact's address: ")
        phone_num = (input("Please enter the contact's phone number: "))
        
        edit_query = "UPDATE contact_table SET fname=%s, lname=%s, address=%s, phone_number=%s WHERE fname=%s"
        val= first_name, last_name, addy,phone_num, edit_contact
        mycursor.execute(edit_query,val)
        db.commit()
        print("Contact edited successfully")
    
    else:
        print("Contact does not exist")
            
# Function that deletes a contact
def delete_contact():
    delete_contact = input("Please enter the name of the contact you want to Delete: ")
    answer = input(f"Are you sure you want to delete {delete_contact} from your contact list(Y/N): ").upper()
    search_query = "SELECT fname FROM contact_table"
    mycursor.execute(search_query)
    
    if (delete_contact,) in mycursor and answer == 'Y':
        
        delete_query = "DELETE FROM contact_table WHERE fname=%s"
        mycursor.execute(delete_query, (delete_contact,))
        db.commit()
        print("Contact was deleted")
    
    else:
        print("Contact doesn't exist in Contact book")
        

def search_contact():
    
    search_contact = input("Please enter the name of the contact you are searching for: ")
    search_query = 'SELECT * FROM contact_table WHERE fname=%s'
    mycursor.execute(search_query, (search_contact,))
    records = mycursor.fetchall()

    print("First Name\t\t\tLast Name\t\t\tAddress\t\t\tPhone Number")
    print("----------\t\t\t---------\t\t\t-------\t\t\t------------")
    
    for first_name, last_name, address, phone_number in records:
        print(f"{first_name}\t\t\t\t{last_name}\t\t\t{address}\t\t\t{phone_number}")
    
