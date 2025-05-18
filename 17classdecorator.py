# class decorator
def add_greeting(cls):
    def greet(self):
        return f"Hello from Decorator! {self.name}"
    cls.greet = greet
    return cls
@add_greeting
class Person:
    def __init__(self,name):
        self.name = name.capitalize()
 # create an instance of class decorator
person = Person ("areeba") 
print(person.greet())         
