from models.department import Department
from models.employee import Employee


def exit_program():
    print("Goodbye!")
    exit()

# We'll implement the department functions in this lesson


def list_departments():
    departments = Department.get_all()
    for department in departments:
        print(department)


def find_department_by_name():
    name = input("Enter the department's name: ")
    department = Department.find_by_name(name)
    print(department) if department else print(
        f'Department {name} not found')


def find_department_by_id():
    # use a trailing underscore not to override the built-in id function
    id_ = input("Enter the department's id: ")
    department = Department.find_by_id(id_)
    print(department) if department else print(f'Department {id_} not found')


def create_department():
    name = input("Enter the department's name: ")
    location = input("Enter the department's location: ")
    try:
        department = Department.create(name, location)
        print(f'Success: {department}')
    except Exception as exc:
        print("Error creating department: ", exc)


def update_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        try:
            name = input("Enter the department's new name: ")
            department.name = name
            location = input("Enter the department's new location: ")
            department.location = location

            department.update()
            print(f'Success: {department}')
        except Exception as exc:
            print("Error updating department: ", exc)
    else:
        print(f'Department {id_} not found')


def delete_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        department.delete()
        print(f'Department {id_} deleted')
    else:
        print(f'Department {id_} not found')


# You'll implement the employee functions in the lab

def list_employees():
    employees = Employee.get_all()
    for employee in employees:
        print(employee)


def find_employee_by_name():
    name = input("Enter employee name: ")
    employee = Employee.find_by_name(name)
    print(employee) if employee else print(
        f"employee {name} not found."
    )


def find_employee_by_id():
    id = input("Enter employee id: ")
    employee = Employee.find_by_id(id)
    print(employee)  if employee else print(
        f"employee with id {id} not found."
    )


def create_employee():
    name = input("Enter employee name: ")
    job = input("Enter Employee Job: ")
    department = input("Enter Employees department id: ")
    try: 
        employee = Employee.create(name, job, int(department))
        print(f"Succes: {employee} created")
    except Exception as exc:
        print("Error creating employee: ", exc)


def update_employee():
    id_ = input("Enter the employee's id: ")
    if employee := Employee.find_by_id(id_):
        try:
            name = input("Enter the employee's new name: ")
            employee.name = name
            job = input("Enter the employee's new job: ")
            employee.job_title = job
            department = input("Enter the employee's new department id: ")
            employee.department_id = department
            
            employee.update()
            print(f'Success: {employee}')
        except Exception as exc:
            print("Error updating employee: ", exc)
    else:
        print(f'Employee {id_} not found')


def delete_employee():
    id = input("Enter employee's id: ")
    if employee := Employee.find_employee_by_id(id):
        employee.delete()
        print(f"Success: {employee} deleted")
    else:
        print(f"Error: {employee} not found")


def list_department_employees():
    dep_id = input("Enter department id: ")
    department = Department.find_by_id(dep_id)
    print(department.employees()) if department else print(f"Error: {dep_id} not found")