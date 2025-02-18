def display_menu():
    print("\nPhoneBook Menu")
    print("1.Add new contact")
    print("2.Search for a cintact")
    print("3.Update contact's Phone number")
    print("4.Delete a contact")
    print("5.List of all contacts")
    print("6.exit")

def add_contact(phonebook):
    name=input("Enter the contact name:")
    if name in phonebook:
        print(f"{name} already exists! in your phonebook with number {phonebook[name]}")
    else:
        phone=input("enter phone number")
        phonebook[name]=phone
        print(f"Contact {name} added successfully")


def search_contact(phonebook):
    name=input("Enter the name to search")
    if name in phonebook:
        print(f"{name}'s phone number is {phonebook[name]}")
    else:
        print(f"Contact {name} not found in the phonebook")

def update_contact(phonebook):
    name=input("Enter the name of the contact you want to update")
    if name in phonebook:
        new_phone=input(f"Enter the new phone number for {name}")
        phonebook[name]=new_phone
        print(f"{name}'s phone number is updated successfully")
    else:
        print(f"Contact {name} not found in your phonebook")

def delete_contact(phonebook):
    name=input("Enter name to delete")
    if name in phonebook:
        del phonebook[name]
        print(f"Contact {name} has been deleted successfully")
    else:
        print(f"Contact {name} not found in your phonebook")

def list_contact(phonebook):
    if not phonebook:
        print("Phonebook is empty")
    else:
        print("\nPhonebook Contact:")
        for name,phone in phonebook.items():
            print(f"Name : {name}, Phone : {phone}")

def main():
        phonebook={}

        while(True):
            display_menu()
            choice=input("Enter Your Choice")

            if choice=="1":
                add_contact(phonebook)

            elif choice=="2":
                search_contact(phonebook)
            elif choice=="3":
                update_contact(phonebook)
            elif choice=="4":
                delete_contact(phonebook)
            elif choice=="5":
                list_contact(phonebook)
            elif choice=="6":
                print("Exiting the Phonebook GoodByee!")
                break
            else:
                print("abbe andhaa hai kya!!")
main()
display_menu()