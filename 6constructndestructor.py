# create a class logger
class Logger:
    # create a constructor
    def __init__(self,id,password):
        self.id = id
        self.password = password
    # create a destructor 
    def __del__ (self):
        print(f"ID name {self.id} has been deleted!!!")   
    # display the login 
    def show_login(self):
        print(f'{self.id} logged in successfully!!!')  
# create an object(instance)
user1 = Logger("Areeba","Areeba1234")
# call the method
user1.show_login()
# explicitly delete the object
del user1

