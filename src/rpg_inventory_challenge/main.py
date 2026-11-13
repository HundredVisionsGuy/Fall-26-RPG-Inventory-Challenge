"""
A prototype for a menu system
"""

# Define functions for your menu options
def do_this():
    """does something"""
    print("You chose this.")

def do_that():
    """does something"""
    print("You did that.")

def choose_me():
    """responds to the choose me option"""
    msg = "\nYou like me; you really like me!!!!"
    msg += "\N{SPARKLING HEART}\N{SPARKLING HEART}\N{SPARKLING HEART}\N{SPARKLING HEART}"
    print(msg)

# Set up the menu system
# Build the menu
menu = "\nGeneric Shopping Market\n\n"
menu += "\t1 - do this\n"
menu += "\t2 - do that\n"
menu += "\t3 - choose me\n"
menu += "\t4 - exit"


# Main loop
# Set sentinel variable to get into menu
user_choice = ""
while user_choice != "4":
    print(menu)
    user_choice = input("Choose a number: ")
    
    # Process user choice
    if user_choice == "1":
        do_this()
    elif user_choice == "2":
        do_that()
    elif user_choice == "3":
        choose_me()
    else:
        print("That is not an option")

print("\nThanks for shopping.")
