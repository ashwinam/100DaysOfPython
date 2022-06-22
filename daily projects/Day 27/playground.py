# create a add function that take number of positional arguments and do sum with those args
# return a tuple or hold a tuple
def add(*args):
    added_values = 0
    for n in args:
        added_values += n
    return added_values


print(add(25, 30, 45, 90, 125, 95))


# **kwargs take unlimited keywords' argument
# return dictionary or hold a dictionary
def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    return n


print(calculate(2, add=20, multiply=30))

class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")


car = Car(make="Nissan", model="GT-R")

print(car.model)

# arguments with default arguments
"""
def my_function(a=1, b=2, c=3):
    # do something
"""
