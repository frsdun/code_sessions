class Person:
    name: str
    age: int

    def __init__(self, my_name: str, my_age: int):
        self.name = my_name
        self.age = my_age

    def talk(self):
        print(f"Hi from {self.name}, they are {self.age} years old")


john = Person("John", 82)


x = 5.5464

print(type(print))
