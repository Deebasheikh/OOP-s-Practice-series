class Person:        #parent class
    def __init__(self,name):     #constructor
        self.name = name
    def display_name(self):
        return("Candidate name is {self.name}.")    
#child class
class Teacher(Person):
    def __init__(self, name,subject_field):
        super().__init__(name)     #call the parent class constructor
        self.subject_field = subject_field 
# over-ride the parent method
    def display_name(self):
        return(f"Teacher's name is {self.name}.\n She has a Master's degree in {self.subject_field}.")     
# create an instance(object)
teacher1 = Teacher("Areeba","Microbiology")  
print(teacher1.display_name())                     
