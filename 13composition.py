# contained object
class Engine:
    def start_engine(self):
        return "engine is starting..."
# container object 
class Car:
    def __init__(self):
        self.engine = Engine()  # Car class (has an Engine inside it) and owns it
    def start_car(self):
        return f"Car is starting: {self.engine.start_engine()}" 
car1 = Car()
print(car1.start_car())           