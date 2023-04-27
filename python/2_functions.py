# ------------------------------------------------------------
# Functions
# ------------------------------------------------------------

def say_hello(first_name, last_name): 
    full_name = first_name + " " + last_name
    print("Hello" + " " + full_name)


def say_hi():
    print("HI!!!!")
    print("Hi again!")
    print("Hi again!!!")


def add_two_numbers(a, b):
    result = a + b
    return result


print(add_two_numbers(1, 20))
print(add_two_numbers(1))
print(add_two_numbers(a=9, b=3))
print(add_two_numbers(b=9, a=3))

say_hello(first_name="Sam", last_name="Suther")


# ------------------------------------------------------------
# Scope
# ------------------------------------------------------------



def add_two_numbers(a,b):
    print("add_two_numbers has been called")
    print(f"a={a}, and is of type {type(a)}")
    print(f"b={b}, and is of type {type(b)}")
    total = a + b
    print(f"total={total}, and is of type {type(total)}")
    return total

add_two_numbers(10,10)
