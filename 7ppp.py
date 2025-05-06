class Employee:
    def __init__(self,name,salary):   #constructor
        self.name = name          #public variable
        self._salary = salary     #protected variable
        self.__ssn = "123456789"      #private variable
# getter method for salary
    def get_salary(self):
        return self._salary
# setter method for salary
    def set_salary(self,amount):
        if amount >= 0:
            self._salary = amount
            print(f'Salary updated to {self._salary}')
        else:
            print(f"Invalid amount.Amount cann't be negative.")    
# getter method for ssn
    def get_ssn(self):
        return "Access denied.SSN is private."        
# method to show the details
    def display_details(self):
        print(f"Name:{self.name} \n Salary:{self._salary}")
# create an instance
employee1 = Employee("abiha",50000)                
employee2 = Employee("ali",70000)
# employee1.display_details()
# access the public attribute
print(f"Name: {employee1.name}")
# access the protected attribute
print(f"{employee1._salary}")
# access the protected attribute through getter n setter method
print(f"Initial balance: {employee1.get_salary()}")
employee1.set_salary(80000)
# access the private method
print(employee1.get_ssn())

# access the public attribute
print(employee2.name)
# access the protected attribute
print(employee2._salary)
# access the protected attribute through getter n setter method
print(f"Initial balance: {employee2.get_salary()}")
employee2.set_salary(100000)
# access the private method
print(employee2.get_ssn())
# display all details
employee2.display_details()


        


