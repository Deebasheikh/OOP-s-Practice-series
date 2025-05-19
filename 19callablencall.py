
class Multiplier:
    def __init__(self,factor):
        self.factor = factor
    def __call__(self):
        number = int(input("Enter a number to multiply: "))  
        result = number * self.factor
        return result
user1 = Multiplier(2)
print(user1())    
print(callable(user1))