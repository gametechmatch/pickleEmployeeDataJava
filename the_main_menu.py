###########################################################################################
# the_main_menu.py
# Author: Lily Zimmermann
# Spring 2022
###########################################################################################
# This program generates the main menu and sends the user input back to the main program
###########################################################################################
def main_menu():
    valid_input = False
    while not valid_input:

        # Print the menu options and get the user choice
        choice = "20"
        choice = (input("___________________________________________________________________\n"
                        "| 1. Look up an employee\n"
                        "| 2. Add a new employee\n"
                        "| 3. Change an existing employee's name, department, and job title\n"
                        "| 4. Delete an employee from the dictionary\n"
                        "| 5. Quit the program and save all changes\n"
                        "___________________________________________________________________\n"
                        )).replace(" ","").replace(".","")

        # Check if the choice equals one of the menu options. Reprint the menu if invalid input
        # is given
        if choice == "1" or choice == "2" or choice == "3" or choice == "4" or choice == "5":
            valid_input = True
        else:
            valid_input = False

    # Convert the choice to an integer
    choice = int(choice)

    # Set up a message that corresponds to the menu choice selected
    if choice == 1:
        choice_message = "Look Up Employee"
    elif choice == 2:
        choice_message = "Add New Employee"
    elif choice == 3:
        choice_message = "Change an Employee's Information"
    elif choice == 4:
        choice_message = "Delete an Employee"
    elif choice == 5:
        choice_message = "Save and Quit"

    # Print message as header for menu option chosen
    print(f"\n*************** {choice}: {choice_message.upper()} ***************")

    # Return the choice and corresponding message to the main program
    return choice
