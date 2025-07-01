# Employee Management System
# This code snippet initializes a simple employee management system using a dictionary to store employee records.
employees = {}
employees[101] = {'name': 'Satya', 'age': 27, 'department': 'HR', 'salary': 50000}


# This code provides a simple command-line interface to manage employee records.
# It allows adding, viewing, and searching for employees in a dictionary structure.
def main_menu():
    def print_menu():
        # This function prints the main menu options for the employee management system.
        print("\nMain Menu:")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Search Employee")
        print("4. Exit")

    flag = True
    while flag:
        print_menu()
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            add_employee()
        elif choice == 2:
            view_employees()
        elif choice == 3:
            search_employee()
        elif choice == 4:
            print("Exiting the system. Thank You!")
            flag = False
        else:
            print("Invalid choice. Please try again.")

def add_employee():
    # This function allows the user to add a new employee to the system.
    global employees

    # Input employee details
    print("\nAdd Employee")
    emp_id = int(input("Enter Employee ID: "))
    name = input("Enter Employee Name: ")
    age = int(input("Enter Employee Age: "))
    department = input("Enter Employee Department: ")
    salary = int(input("Enter Employee Salary: "))

    # Check if employee ID already exists
    if emp_id in employees:
        print("Employee ID already exists. Please try again.")
        emp_id = int(input("Enter Employee ID: "))

    employees[emp_id] = {'name': name, 'age': age, 'department': department, 'salary': salary}
    print(f"Employee {name} added successfully with ID {emp_id}.")

def view_employees():
    # This function displays all employees in the system.
    global employees
    print("\nView Employees")
    if not employees:
        print("No employees available.")
        return
    print("List of Employees:")
    # Display all employees
    print("ID\tName\tAge\tDepartment\tSalary")
    print("-" * 50)
    for emp_id, details in employees.items():
        print(f"{emp_id}\t{details['name']}\t{details['age']}\t{details['department']}\t{details['salary']}")

def search_employee():
    # This function allows the user to search for an employee by ID.
    global employees
    print("\nSearch Employee")
    emp_id = int(input("Enter Employee ID to search: "))
    if emp_id in employees:
        details = employees[emp_id]
        print(f"Employee Found: ID: {emp_id}, Name: {details['name']}, Age: {details['age']}, "
              f"Department: {details['department']}, Salary: {details['salary']}")
    else:
        print("Employee not found.")

# Start the employee management system
if __name__ == "__main__":
    print("Welcome to the Employee Management System!")
    print("Initializing the system...")
    print("Employee ID 101 is already added with details: Name: Satya, Age: 27, Department: HR, Salary: 50000")
    main_menu()