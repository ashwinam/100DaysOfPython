# class Inheritance

class Animal:
    def __init__(self):
        self.num_of_eyes = 2

    def breath(self):
        print("Inhale, Exhale")


class Fish(Animal):
    def __init__(self):
        super().__init__()  # its like Animal.__init__

    def breath(self):
        super().breath()  # I say execute previous or super class method
        print("Inside the water.")

    def swim(self):
        print("moving inside water.")


nemo = Fish()

nemo.swim()
nemo.breath()
nemo.num_of_eyes = 5
print(nemo.num_of_eyes)

# So final note is that Inheritance plays a big role in OOP, basically i say inherit the appearance(attributes) and
# behaviour(methods) from the super class, in here animal is super class.
