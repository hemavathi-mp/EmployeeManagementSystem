

# Employee class
class Employee:
  def __init__(self, name, employee_id, department, title):
      # Initialize the attributes
      self.name = name
      self.employee_id = employee_id
      self.department = department
      self.title = title

  def __str__(self):
      # Implement a string representation method that returns the employee's name and ID.
      print(f"Name: {self.name}, ID: {self.employee_id}")

  def __repr__(self):
      # Implement a string representation method that returns the employee's name and ID.
      print(f"Name: {self.name}, ID: {self.employee_id}")

  def get_details(self):
      # Print the details of the employee
      print(f"Name: {self.name}, ID: {self.employee_id}, Department: {self.department}, Title: {self.title}")



class Department:
  def __init__(self,dept_id, d_name, employee_name):
      # Initialize the attributes
      self.dept_id = dept_id
      self.d_name = d_name
      self.employee_name = employee_name


  def get_details(self):
      # Print the details of the employee
      print(f"Department ID: {self.dept_id}, Department Name: {self.d_name}, Employee: {self.employee_name}")

# EmployeeManagement class
class EmployeeManagement:
  def __init__(self):
      # Initialize the list of employees and departments
      self.employees = []
      self.department = []

  def add_employee(self, employee):
      # Add an employee to the list
      self.employees.append(employee)

  def remove_employee(self, employee_id):
      # Remove an employee from the list
      # self.employees = [employee for employee in self.employees if employee.employee_id != employee_id]
      for i, employee in enumerate(self.employees):
          if employee.employee_id == employee_id:
            del self.employees[i]

  def display_all_employees(self):
      # Display all employees
      for employee in self.employees:
        employee.get_details()

  # __________________________Department_____________________________

  def add_department(self, department):
      # Add an department to the list
      self.department.append(department)

  def remove_department(self, id):
      # Remove an employee from the list
      for i, dept in enumerate(self.department):
          if dept.dept_id == id:
            del self.department[i]

  def display_all_department(self):
      # Display all employees
      for dept in self.department:
        dept.get_details()

  # __________________________End_____________________________

  def display_repr_employees_name_id(self):
      # Display __repr__ employees name and ID
      for employee in self.employees:
        employee.__repr__()

  def display_str_employees_name_id(self):
      # Display __str__ employees name and ID
      for employee in self.employees:
        employee.__str__()

# Demonstrate the functionality
# Create some Employee objects
print("Enter Employee details:\n")
employee1 = Employee(input("Enter Employee Name\t:"), int(input("Enter employee_id\t:")), input("Enter department\t:"), input("Enter title\t:"))
employee2 = Employee(input("Enter Employee Name\t:"), int(input("Enter employee_id\t:")), input("Enter department\t:"), input("Enter title\t:"))
# employee1 = Employee("John", 1, "Department", "Software Engineer")
# employee2 = Employee("Jane", 2, "Testing", "HR Manager")

# Create an EmployeeManagement object
employee_management = EmployeeManagement()

# Add the employees to the EmployeeManagement object
employee_management.add_employee(employee1)
employee_management.add_employee(employee2)

# Display employees name and ID
print("String representation method (__repr__) that returns the employee's name and ID.")
employee_management.display_repr_employees_name_id()

print("String representation method (__str__) that returns the employee's name and ID.")
employee_management.display_str_employees_name_id()

# Display all employees
print("All Employees:")
employee_management.display_all_employees()

# Remove an employee
employee_management.remove_employee(int(input("Enter employee_id to remove\t:")))

# Display all employees
print("All Employees after removal:")
employee_management.display_all_employees()

# ____________________department read, add, remove operations__________________
print("------------------------------------------------------------------------------")
print("Enter Department details:\n")
department1 = Department(int(input("Enter dept_id\t:")), input("Enter Department Name\t:"), input("Enter employee_name\t:"))
department2 = Department(int(input("Enter dept_id\t:")),input("Enter Department Name\t:"), input("Enter employee_name\t:"))
# department1 = Department(111, "Testing", "Jane")
# department2 = Department(112, "Development", "John")

# Create an Department object
department_data = EmployeeManagement()

# Add the department to the EmployeeManagement object
department_data.add_department(department1)
department_data.add_department(department2)

# Display all Department
print("All Department:")
department_data.display_all_department()

# Remove an department
department_data.remove_department(int(input("Enter department ID  to remove\t:")))

# Display all department
print("All Eepartment after removal:")
department_data.display_all_department()


