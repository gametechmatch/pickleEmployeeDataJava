###########################################################################################
# employee_management_system.py
# Author: Lily Zimmermann
###########################################################################################
# This is the main program that runs all code
###########################################################################################

# Import code from external files
from employee import *
from pickle_functions import *
from user_validation import *
import the_main_menu

###########################################################################################
# This  function is the main function that runs all code
###########################################################################################
def main():
    # Open file (or create file) that will hold pickled employee data
    employees = open_employee_data()

    # Message that prints out the name of the program
    print("############################################################################")
    print("#\t\t\t\t\t\t\tEMPLOYEE MANAGEMENT SYSTEM\t\t\t\t\t   #")
    print("############################################################################\n")

    # A message to explain the main menu
    print(f"Please choose one of the following menu options.\n"
          "Enter the number that corresponds with your choice:\n")

    # Beginning of program loop
    working = True
    while working:
        # Find out menu choice for user
        choice = the_main_menu.main_menu()

        # Process the menu option chosen by the user
        if choice == 5: # Save data and end program if user enters 5
            print(f"Saving employee data . . . \n")
            working = False
        else: # Otherwise proceed with program
            employees = menu_router(choice, employees)

    # Save the employee data changes to the file and terminate program
    save_employee_data(employees)
    print("Employee data saved")

###########################################################################################
# This  function routes the code to the correct sub-function depending on the menu choice
###########################################################################################
def menu_router(choice, employees):
    if choice == 1:
        choice_message = "lookup"
        employees = lookup_employee(choice_message, employees)
        # Return to the main menu after done looking up
        return employees
    elif choice == 2:
        choice_message = "add"
        employees = add_employee(choice_message, employees)
        # Return to the main menu after done adding
        return employees
    elif choice == 3:
        choice_message = "change"
        employees = change_employee(choice_message, employees)
        # Return to the main menu after done changing
        return employees
    elif choice == 4:
        choice_message = "delete"
        employees = delete_employee(choice_message, employees)
        # Return to the main menu after done deleting
        return employees
    else:
        print("Menu Router Error")
        # Return to the main menu if error occurred
        return employees
###########################################################################################
# This  function handles all lookup requests
###########################################################################################
def lookup_employee(choice_message, employees):
    # Check if the dictionary "employees" is empty, if so, return to main menu
    current_dict_status = check_if_dictionary_empty(choice_message, employees)
    if current_dict_status == "empty":
        return employees

    # Proceed if dictionary "employees" not empty
    still_looking_up = True
    while still_looking_up:

        # Ask user for employee ID
        employee_id = validate_employee_id(choice_message)

        # Return to main menu if user entered x for exit
        if employee_id == "x":
            return employees

        # Print employee information if ID already exists or
        # print a message if the ID couldn't be found
        if employee_id not in employees:
            print("\nI'm sorry. I could not find that employee")
        else:
            print(f"{Employee.get_employee(employee_id, employees)}")

        # Ask user if they want to look up another employee
        user_input = try_again_confirmation(choice_message)

        # Exit to main menu if user entered n for no
        if user_input == "n":
            return employees

###########################################################################################
# This  function handles all add requests
###########################################################################################
def add_employee(choice_message, employees):
    still_adding_employees = True
    while still_adding_employees:

        # Obtain employee ID from user
        employee_id = validate_employee_id(choice_message)

        # Return to main menu if user enters x to exit
        if employee_id == "x":
            return employees

        # Check if dictionary "employees" contains any key value pairs
        if employees:
            # Print out employee info if ID already exists
            if employee_id in employees:
                print(f"Employee {employee_id} is already in the list.\n")
                print(f"{Employee.get_employee(employee_id, employees)}")
                decision_to_add = "n"

            # Collect applicable info if ID doesn't already exist
            else:
                employee_name, employee_department, employee_job_title = \
                    obtain_employee_information()

                # Confirm that user wants to proceed with change
                decision_to_add = final_choice_confirmation(choice_message,
                                                            employee_id,
                                                            employee_name,
                                                            employee_department,
                                                            employee_job_title)

        # If dictionary "employees" is empty collect all applicable info
        else:
            employee_name, employee_department, employee_job_title = \
                obtain_employee_information()

            # Confirm that user wants to proceed with change
            decision_to_add = final_choice_confirmation(choice_message,
                                                        employee_id,
                                                        employee_name,
                                                        employee_department,
                                                        employee_job_title)
        # Add new employee if user verifies y for yes
        if decision_to_add == "y":
            Employee.add_employee(employee_id, employee_name, employee_department,
                                  employee_job_title, employees)

        # Ask user if they want to add another employee
        user_input = try_again_confirmation(choice_message)

        # Exit to main menu if user enters n for no
        if user_input == "n":
            return employees

###########################################################################################
# This  function handles all change requests
###########################################################################################
def change_employee(choice_message, employees):
    # Check if the dictionary "employees" is empty, if so, return to main menu
    current_dict_status = check_if_dictionary_empty(choice_message, employees)
    if current_dict_status == "empty":
        return employees

    # Proceed with change if dictionary "employees" is not empty
    still_changing = True
    while still_changing:

        # Obtain employee ID number that should be updated
        employee_id = validate_employee_id(choice_message)

        # Exit to main menu if user entered x for exit
        if employee_id == "x":
            return employees

        # Print out message if ID does not exist yet
        if employee_id not in employees:
            print("I'm sorry. That employee does not exist in the system.\n")

        # Proceed with change if ID exists
        else:

            # Print the employee info
            print(f"Thank you! That employee ID corresponds to the individual below:\n")
            print(f"\n{Employee.get_employee(employee_id, employees)}")

            # Confirm if user wants to proceed to change selected employee
            decision_to_change = simple_choice_confirmation(choice_message)

            # If user enters y for yes, proceed with change
            if decision_to_change == "y":
                print(f"Please enter all information for employee {employee_id}")

                # Collect the applicable information
                employee_name, employee_department, employee_job_title \
                    = obtain_employee_information()

                # Confirm if employee ID should be updated with the user entered info
                change_decision = final_choice_confirmation(choice_message,
                                                            employee_id,
                                                            employee_name,
                                                            employee_department,
                                                            employee_job_title)

                # If user confirms change, update the employee
                if change_decision == "y":
                    Employee.change_employee(employee_id, employee_name, employee_department,
                                             employee_job_title, employees)

        # Find out if user wants to change additional employees
        decision_to_continue_changing = try_again_confirmation(choice_message)

        # Exit to main menu if user enters n for no
        if decision_to_continue_changing == "n":
            return employees

###########################################################################################
# This  function handles all deletion requests
###########################################################################################
def delete_employee(choice_message, employees):
    still_deleting = True
    while still_deleting:

        # Check if the dictionary "employees" is empty, if so, exit to main menu
        current_dict_status = check_if_dictionary_empty(choice_message, employees)
        if current_dict_status == "empty":
            return employees

        # Obtain ID from user if dictionary not empty
        employee_id = validate_employee_id(choice_message)

        # Exit to main menu if user entered x to exit
        if employee_id == "x":
            return employees

        # Print message if ID does not exist
        if employee_id not in employees:
            print("I'm sorry. That ID does not exist.")

        # Proceed with deletion if ID exists
        else:
            # Print out employee information for ID found
            print("\nThank you!\n")
            print("You selected the following employee:")
            print(f"{Employee.get_employee(employee_id, employees)}")

            # Confirm if user wants to delete the employee found
            user_input = simple_choice_confirmation(choice_message)

            # Delete employee if user enters y for yes
            if user_input == "y":
                Employee.delete_employee(employee_id, employees)

        # Ask if user wants to delete another employee
        user_input = try_again_confirmation(choice_message)

        # Exit to main menu if user enters n for no
        if user_input == "n":
            return employees

###########################################################################################
# This  function checks if the dictionary "employees" is empty
###########################################################################################
def check_if_dictionary_empty(choice_message, employees):
    if employees:
        return "not_empty"
    else:
        print("I'm sorry. The dictionary is currently empty."
              f"There are no employees to {choice_message}")
        return "empty"

#Execute main program
if __name__ == '__main__':
    main()
