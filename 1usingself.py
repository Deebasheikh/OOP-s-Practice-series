class Student:
    def __init__(self,name,marks):
        self.name = name  #instance variable
        self.marks = marks
        

    def display(self):
        print(f"Student name is {self.name.capitalize()}. {self.name.capitalize()} scored {self.marks} marks.")
        # print(self.name, "scored", self.marks, "marks.")   
        
student1 = Student("ali",89)
student2 = Student("areeba",95)
student1.display()
student2.display()
    

        