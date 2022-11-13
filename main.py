# student information
"""
addressbook.py
A Program to Collect Information on Contacts
Programmed by: Ireanne Omega
Version Created: 01-13-2022

"""
# ......................................All rights received.................................................
 # introductiong
print(".....................................")
print("----CONTACT FlIGHT TRACKER ---")
print("Note: This is mandatory for all")
print("travelers entering any countries.")
print("---PLEASE FILL UP ACCORDINGLY---")
print(".....................................")

# ...L I S T & V A R I A B L E S...........................................................................
# Variables
contacts = []
contactTracking = []

# User input
def contact_tracking():
    print(" ")
    print('=' * 132)
    print(f"\t\t\t{'FIRST NAME': <20s}{'LAST NAME': <20s}{'COMPLETE ADDRESS': <60s}{'PHONE NUMBER': <15s}")
    print('=' * 132)

#.... F U N C T I O N S....................................................................................
# Display Main Menu
def menu():
    print("\n")
    print('' * 5, "CONTACT TRACING PROGRAM", '' * 5)
    print("What would you like to do?")
    print("[1] Add Contact")
    print("[2] Search Contact")
    print("[3] Exit")


#Function used to add contact
# Menu option1
def add_contact():
    while True:
        print("\n")
        print('' * 18, "Adding Contacts in Contact Information", '' * 18)
        first_name = input("First Name: ")
        last_name = input("Last Name: ")
        address = input("Address: ")
        number = input("Contact Number: ")
        contactInformation = f"\t{first_name: <20}{last_name: <20}{address: <60}{number: <15}"
        contacts.append(contactInformation)

      # For Loop Functions
        add = input("Would you like to add another contact? (y / n): ")
        if add == 'y':
            continue
        elif add == 'n':
            runProgram()
        else:
            print("Choose a valid option.")
            runProgram()


# Function Used to Search Contact
#Menu option2
def search_contact():
    while True:
        print("\n")
        print('*'* 18, "Search for Contacts", '*' * 18)
        search = input("Choose information you want to search. \n"
                            "[a] First Name \n"
                            "[b] Last Name \n"
                            "[c] Address \n"
                            "[d] Contact Number \n"
                            "Option: ")

        # search first name
        if search.casefold() == 'a':
                search_first = input("Enter the first name you want to search: ")
                count = 0
                contact_tracking()
                for contact in contacts:
                    if search_first in contact:
                        count += 1
                        print("\t\t", contact)
                        print('=' * 132)
                if count == 0:
                    print("First Name Unavailable {0]".format(search_first))


        # search last name
        elif search.casefold() == 'b':
                search_last = input("Enter the last name you want to search: ")
                count = 0
                contact_tracking()
                for contact in contacts:
                    if search_last in contact:
                        print("\t\t", contact)
                        print('=' * 132)
                        count += 1
                if count == 0:
                    print("Last Name Unavailable {}".format(search_last))


        # search address
        elif search.casefold() == 'c':
                search_add = input("Enter the address you want to search: ")
                count = 0
                contact_tracking()
                for contact in contacts:
                    if search_add in contact:
                        print("\t\t", contact)
                        print('-' * 132)
                        count += 1
                if count == 0:
                    print("No contact found with the provided address: {0}".format(search_add))

        # search contact number
        elif search.casefold() == 'd':
                search_num = input("Enter the contact number you want to search: ")
                count = 0
                contact_tracking()
                for contact in contacts:
                    if search_num in contact:
                        print("\t\t", contact)
                        print('-' * 132)
                        count += 1
                if count == 0:
                    print("No contact found with the provided contact number: {0}".format(search_num))


        # for loop function 2
        try_again = input("\nWould you like to search another contact? (Yes or No) :")
        if try_again == 'Yes':
                continue
        elif try_again == 'No':
                runProgram()
        else:
                print("Choose another option. Please try again!")
                runProgram()


#Function Used to Exit Program
#Menu Option3
def exit_program():
    while True:
        print("\n")
        print('' * 18, "Exit Program", '' * 18)
        exOption = input("Do you want to close this program? (y / n): ")

        if exOption == 'y':
            print("Thank you for cooperating with us. Pls stay safe!")
            print("--------------------------------------------------")
            exit()
        elif exOption == 'n':
            runProgram()
        else:
            print("Error. Choose the right option.")
            continue

# To run the program, i must use these functions
def runProgram():
    while True:
        menu()
        choice = int(input("Choose an option: "))

        if choice == 1:
            add_contact()
        elif choice == 2:
            search_contact()
        elif choice == 3:
            exit_program()
        else:
            print("Invalid Choice. Try again!")
            continue

while True:
    runProgram()

