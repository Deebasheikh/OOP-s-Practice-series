class Dog:
    def __init__(self,name,breed):
        self.name = name
        self.breed = breed
    def bark(self):
        print(f"{self.name} is a dog's name and belongs to {self.breed} breed.")    
dog1 = Dog("Simba","Boxer")
dog2 = Dog("Emma","American Eskimo Dog")        
dog1.bark()
dog2.bark()
        