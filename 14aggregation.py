class Employee:
    def __init__(self,name):
        self.name = name
class Department:
    def __init__(self,name):        
        self.name = name
        self.employees = []       #department 'has a' employee but doesnot own it
    def add_employee(self,employee):
        self.employees.append(employee)
employee1 = Employee("arif")
department = Department("microbiology")        
department.add_employee(employee1)
    # print te employess
for employee in department.employees:
 print(employee.name)    
