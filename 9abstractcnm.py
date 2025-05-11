from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass
class Rectangle(Shape):
    def __init__(self,side):
        self.side = side
    def calculate_area(self):
        return self.side * self.side

rectangle1 : Rectangle = Rectangle(4)  
rectangle2 : Rectangle = Rectangle(8)           
print(f"The area of rectangle is {rectangle1.calculate_area()}.")
print(f"The area of rectangle is {rectangle2.calculate_area()}.")