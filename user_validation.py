###########################################################################################
# user_validation.py
# Author: Lily Zimmermann
# Spring 2022
###########################################################################################
# This program handles most user validation for the main program
###########################################################################################

###########################################################################################
# This function returns all employee info entered by user and asks if change should proceed
# This is used when the user_input info has not been saved to the dictionary titled
# "employees" yet
###########################################################################################
def final_choice_confirmation(choice_message, employee_id, employee_name,
                              employee_department, employee_job_title):
    waiting_for_valid_input = True
    while waiting_for_valid_input:
        # Print out employee info entered by user
        print("\nYou entered:")
        print(f"__________EMPLOYEE: {employee_id}__________\n"
              f'Name: {employee_name}\nDepartment: {employee_department}\n'
              f'Job Title: {employee_job_title}\n')

        # Ask user if program should continue with change
        change_decision = input(f"Y = {choice_message} employee\n"
                                f"N = No do not {choice_message} employee:\n"
                                ).lower().replace(" ", "").replace(".", "")

        # If user enters valid input, return to the program using this function
        if change_decision == "y" or change_decision == "n":
            return change_decision

        # Print message and return to beginning of loop if invalid input entered
        else:
            print("I'm sorry. I don't understand.")

###########################################################################################
# This function asks user if the program should continue with a change when the data
# entered cannot be pulled from the "employees" dictionary
###########################################################################################
def simple_choice_confirmation(choice_message):
    waiting_for_valid_input = True
    while waiting_for_valid_input:
        # Print out info entered by user and ask if change should continue
        print(f"Do you want to {choice_message} the selected employee?")
        user_choice = input(f"Y = {choice_message} employee\n"
                            f"N = No do not {choice_message} employee:\n"
                            ).lower().replace(" ", "").replace(".", "")

        # If user enters valid input, return to the program using this function
        if user_choice == "y" or user_choice == "n":
            print("\nSounds good.\n")
            return user_choice

        # Print message and return to beginning of loop if invalid input entered
        else:
            print("I'm sorry. I don't understand.")

###########################################################################################
# This function asks user if the program should exit to the main menu or loop back and
# let the user try the same menu option that was originally chosen
###########################################################################################
def try_again_confirmation(choice_message):
    waiting_for_valid_response = True
    while waiting_for_valid_response:
        # Ask user if they want to return to main menu or repeat selected menu option
        print("___________________________________________________________________\n"
              f"|Do you want to {choice_message} an additional employee?")
        user_input = input(f"|Y = yes\n|N = no\n"
                           "___________________________________________"
                           "________________________\n"
                           ).lower().replace(" ", "").replace(".", "")

        # If user enters valid input, return to the program using this function
        if user_input == "y" or user_input == "n":
            return user_input

        # Print message and return to beginning of loop if invalid input entered
        else:
            print("\nI'm sorry. I did not understand.\n")

###########################################################################################
# This function validates an employee ID
###########################################################################################
def validate_employee_id(choice_message):
    employee_id = "z"
    while not employee_id.isdigit():
        # Ask for employee number
        employee_id = input("___________________________________________"
                            "________________________\n"
                            f"Please enter the ID number for the employee to {choice_message}.\n"
                            'or enter "X" to exit to main menu\n'
                            "___________________________________________"
                            "________________________\n").lower()

        # If user enters valid input, return to the program using this function
        if employee_id == "x" or employee_id.isdigit():
            return employee_id

        # Print message and return to beginning of loop if invalid input entered
        else:
            print("""\nI'm sorry. That is not a number or an "X" to exit\n""")
###########################################################################################
# This function obtains employee information to add or update an employee
###########################################################################################
def obtain_employee_information():
    # Ask user for employee first name
    employee_first_name = "1"
    while not employee_first_name.replace(" ", "").isalpha():
        employee_first_name = input("Employee First Name: ").upper()

    # Ask user for employee last name
    employee_last_name = "2"
    while not employee_last_name.replace(" ", "").isalpha():
        employee_last_name = input("Employee Last Name: ").upper()

    # Put first and last name together
    employee_name = f"{employee_first_name} {employee_last_name}"

    # Ask user for employee department
    employee_department = "1"
    while not employee_department.replace(" ", "").isalpha():
        employee_department = input("Employee Department: ").upper()

    # Ask user for employee job title
    employee_job_title = "1"
    while not employee_job_title.replace(" ", "").isalpha():
        employee_job_title = input("Employee Job Title: ").upper()

    # Return to program using this function
    return employee_name, employee_department, employee_job_title
