class Car:
    def __init__(self,brand):
        self.brand  = brand #PUBLIC ATTRIBUTE

    def start(self):
        print(f"Start your {self.brand}.") 

# instantiate the class
car1 = Car("BMW") 
# access the pulic method
car1.start()  
# access the public variable
print(f"Car brand is {car1.brand}")

