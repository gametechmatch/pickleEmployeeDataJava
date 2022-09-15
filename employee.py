########################################################################
# employee.py
# Author: Lily Zimmermann
########################################################################
# This file holds the employee class
########################################################################

class Employee:

    # The __init__ method accepts an employee ID  as an argument for the
    # name, department, and job of an employee
    def __init__(self, employees):
        this_employee = list(employees[self])
        self.name = this_employee[0]
        self.dept = this_employee[1]
        self.job_title = this_employee[2]

    # This method prints out all the information for an exiting employee
    def get_employee(self, employees):
        this_employee = list(employees[self])
        return f"__________EMPLOYEE: {self}__________\n" \
               f'Name: {this_employee[0]}\nDepartment: {this_employee[1]}\n' \
               f'Job Title: {this_employee[2]}\n'

    # This method adds an employee to the "employees" dictionary
    def add_employee(self, name, department, job_title, employees):
        employees[self] = [f'{name}', f'{department}', f'{job_title}']
        print("\nEmployee Added:")
        print(f"{Employee.get_employee(self, employees)}\n")

    # This method changes an existing employee in the "employees" dictionary
    def change_employee(self, name, department, job_title, employees):
        employees[self] = [name, department, job_title]
        print(f"\nEmployee {self} Changed\n")

    # This method deletes an existing employee from the "employees" dictionary
    def delete_employee(self, employees):
        if self in employees:
            del employees[self]
            print(f"\nEmployee {self} Deleted\n")
