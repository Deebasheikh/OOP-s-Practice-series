def log_function_call(fnc):
    def wrapper(*args,**kwargs):
     print("function is being called")
     return fnc(*args,**kwargs)
    return wrapper

@log_function_call
def say_hello(name,greeting= "hello"):
    print(f"{greeting.capitalize()} {name.capitalize()}!")

say_hello("areeba",greeting="salam")    