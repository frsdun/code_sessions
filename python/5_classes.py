# 1. A way to group data and functions.
#    - Reuse code
#    - Create your own logical "things" to work with

# 2. Class vs object. Blueprint vs the actual houses
#    - A Class is like an architects blueprint, it defines the shape of the
#      thing that is going to exist later.
#    - An object is an instance of a Class, like the house that has been
#      build according to a blueprint.


# %%


class Person:
    name = "John"
    age = 73

    def talk(self):
        print(f"Hi from {self.name}")


john_ojb = Person()
other_person = Person()

john_ojb.talk()
other_person.talk()
print(john_ojb.name)


# %%


class Person:
    name: str
    age: int

    def __init__(self, my_name: str, my_age: int):
        self.name = my_name
        self.age = my_age

    def talk(self):
        print(f"Hi from {self.name}, they are {self.age} years old")


sally = Person("Sally", 13)
bob = Person("Bob", 82)

sally.talk()
bob.talk()


# %% Inheritance


class Vehicle:
    def go(self):
        print("Brr [Sound of Vehicle]")


class Car(Vehicle):
    pass


class Bicycle(Vehicle):
    def go(self):
        print("Squeak, squeak... [Sound of a Bicycle]")


jeep = Car()
trek = Bicycle()

bus = Vehicle()
bus.go()
jeep.go()
trek.go()


# %% Mixins (multiple inheritance)


class Adder:
    def add(self, x: int, y: int):
        return x + y

    def add_2(self, x: int):
        return x + 2


class Multiplier:
    def multiply(self, x: int, y: int):
        return x * y

    def square(self, x: int):
        return x * x


class Calculator(Adder, Multiplier):
    """This is my calculator"""

    def do_maths(self, x: int, y: int):
        return round(self.add(x, y) + self.square(x))


calc = Calculator()

print(calc.add(1, 2))
print(calc.multiply(1, 2))
print(calc.do_maths(1, 2))

# %%
