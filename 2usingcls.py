class Counter:
    count = 0

    def __init__(self,name,marks):
        self.name = name  #instance variable
        self.marks = marks

    # instance method
    def display(self):
        print(f"Student name is {self.name.capitalize()}. {self.name.capitalize()} scored {self.marks} marks.")
        Counter.count += 1
    # class method
    @classmethod
    def display_count(cls):
        print(f"Total students are {cls.count}") 

student1 = Counter("ali",89)
student2 = Counter("areeba",95)

student1.display()
student2.display()
Counter.display_count()