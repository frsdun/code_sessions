# 1. A way to group data and functions.
#    - Reuse code
#    - Create your own logical "things" to work with

# 2. Class vs object. Blueprint vs the actual houses
#    - A Class is like an architects blueprint, it defines the shape of the
#      thing that is going to exist later.
#    - An object is an instance of a Class, like the house that has been
#      build according to a blueprint.


# %% Class vs instance
class Person:
    name = "John"

    def talk(self, text: str):
        print(self.name + " says: " + text)


john_obj = Person()
john_obj.talk("Hi!")

print(john_obj.name)

type(john_obj)
isinstance(john_obj, Person)


# %% Constructor / initializer
class Person:
    name = "Unnamed"

    def __init__(self, persons_name: str):
        self.name = persons_name

    def talk(self, text: str):
        print(self.name + " says: " + text)


sally = Person("Sally")
sally.talk("Wow!")

barbra = Person("Barbra")
barbra.talk(f"My name is {barbra.name}")

# %% Inheritance


class Vehicle:
    def __init__(self, color: str):
        self.color = color

    def start_moving(self):
        print("Brr! [Engine sounds]")

    def identify(self):
        print(f"{self.color} Vehicle")


class Car(Vehicle):
    def identify(self):
        print(f"{self.color} Car")


class Bicycle(Vehicle):
    def start_moving(self):
        print("Squeak, squeak... [Peddling sounds]")

    def identify(self):
        print(f"{self.color} Bicycle")


jeep = Car("Green")
trek = Bicycle("Silver")

jeep.start_moving()
jeep.identify()

trek.start_moving()
trek.identify()

print("Type of jeep:", type(jeep))
print("Type of trek:", type(trek))

print("Is the trek in instance of a Bicycle:", isinstance(trek, Bicycle))
print("Is the trek in instance of a Vehicle:", isinstance(trek, Vehicle))
print("Is the trek in instance of a Car:", isinstance(trek, Car))

# %% Mixin


class CanAdd:
    def add(self, x: int, y: int):
        return x + y


class CanMultiply:
    def multiply(self, x: int, y: int):
        return x * y


class Calculator(CanAdd, CanMultiply):
    pass


calculator = Calculator()

print(calculator.add(1, 2))
print(calculator.multiply(1, 2))


# %% Everything in python is actually an instance of a class

print("strings:", type("A literal string"))
print("numbers:", type(5))

x = 6
print("number x:", type(x))


def add(a: int, b: int):
    return a + b


print("functions add:", type(add))
print("functions add called:", type(add(1, 2)))
print("built in functions:", type(print))


# %%
