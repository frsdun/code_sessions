# Introduction

In this series of sessions we are going to learn the fundamentals of programming.

Programming is actually pretty simple once you understand a small set of fundamental concepts.

Many programming languages share these same concepts so once you learn how to use one language it's much easier to pick up another.

Our goal is to get over the initial hurdles so you can start teaching yourself to code if you wish

We are going to be learning Python.

Python is a popular high-level, dynamically typed, and interpreted language.
By the end of this session you will know what all those words actually mean.

The core concepts we will cover in the sessions will be roughly:

- Variables and memory
- Data types
- Operators
- Functions
- Control flow
- Loops
- Scope
- Classes
- Exceptions
- Modules and libraries

## Starting at the beginning

Let start at the computer.
For the sake of simplicity we can think of a computer as a machine that can do three things, read our inputs, run programs and display information.
We don't need to care about the CPU architecture, binary code, operating system and so on, to us commuters run programs.

> Side note: This idea of hiding complexity inside a simplified exterior is called "abstraction" and we are going to come across it a lot.
> Abstraction is wonderful because we can understand and do a lot without needing to wade through the details.
> We don't need to think about the value timing in the cars engine when we accelerate, we just push the peddle down.

So computers run programs and we are going to be telling it to run the program called "python" or more correctly "the python interpreter".

The program called "python" reads text files containing instructions in a particular format and then executes those instructions line be line.

The text files here is our python code and this code needs to be written in the python language so that the python interpreter can understand it.

So our python text files are run by the python interpreter, making Python an interpreted language.

> Side note: Some languages are not interpreted, they are "compiled".
> Instead of having a program interoperate your code as you run it, a compiled language has an extra step you have to do before it can be run.
> First your code is fed into a compiler that creates (compiles) a program from your code, then you run this new program.

Here is an example of some python code. You don't need to understand any of it now, but soon you will know what every character does.

```py
# Create a sentence from a list of words

word_list = []

word_list.append("A")
word_list.append("dog")

sentence = ""

for word in word_list:
    sentence = sentence + " " + word

print(sentence)
# Output: " A dog"
```

## Variables and memory

Lets write our first python program!

```py
my_favorite_color = "green"
```

Our program contains one statement/instruction: store the word "green" in a variable called "my_favorite_color".
If we run this program, the word "green" is stored in memory until the program gets the the end on the instruction and then clears its memory.
So it's a useless program.

In python the equals sign `=` is actually called the assignment operator. It has nothing to do with comparing how equal the two side are.
The technically correct description of this statement is: Assign the string "green" to the variable called "my_favorite_color"

The first time a understood how variables works is when it was explained like this.

Imagine a man standing at a counter with two shelves behind him, this man is your computers memory register.
You go to the man and ask him to store your house keys, he gets a small box from the shelf behind him, puts your keys in it then asks you what label you want to give this box, lets say "house_keys". Later when you want your keys back you you got to the man and ask for the box labeled "house_keys", he then find the box in the shelves behind him and give you back your keys.
In this metaphor the labeled box is the variable and the value it contains is the keys.
In our useless program above, we asked the man at the counter to store the word "green" in a box called "my_favorite_color", then left.

The man at the counter actually has a veritably of different container types. If you ask him to store a liter milk, he will use a bottle not a box.
So there are different types of data we need to store in memory. Keys, noodles and milk translate or integers, string and booleans.

In some languages you have to specify the size of the box you need upfront, but in python if you ask the man at the counter to store a pool noodle he will get a pool noodle sized box. The if you take the pool noodle out and switch it for a spade full of lava he will automatically change it for an approbated type of container. Some languages will just crash with an error message like "You can't store a lava in a pool noodle box!"
This is why we say python is a dynamically type language because we can use the same variable (labeled container) to store different types of values (noodles, laval) and python will automatically adjust the memory allocation. Python will also automatically delete values you are no longer using, so you don't fill up your computers memory with old data you no longer need.

In summary, we can store values in variables which are labeled containers and the values we store have a type.

Variables must stat with an alphabetical letter and contain no spaces.
By convention python uses `snake_case` for variable names.
Some special characters are allowed but not all. You can google which ones.

Example variable names:

```py
# Valid
a = 1
some_long_collection_of_words = 1
text_3 = 1
CamelCase = 1
pascalCase = 2

# Invalid
24hours = 1
@_address = 1
some name = 1
some-name = 1
```

## Data types

Every value or bit of data has a type. Here are some examples type:

```py
# Integer (int)
var_a = 42
var_b = -12723
var_c = 0

# String (str). For storing text
var_d = "a string is just a string characters"
var_e = "42"
var_f = ""
var_g = 'A string can use single or double quotes'

# Boolean (bool)
var_h = True
var_i = False

# Float. Numbers with a decimal point
var_j = 42.95
var_k = -12.723
var_l = 0.0

# List. An array of values, each with their own type
var_m = [1, 4, 5, 9, 2]
var_n = ["a", "list", "of", "strings"]
var_o = ["a", 34, True, 13.9]

# Dictionary (dict). A collection of values stored against a key. Here "name" is the key that stores the string value "Mont Blanc"
var_p = {
    "name": "Mont Blanc",
    "height_meters": 4807.81,
    "height_feet": 15774,
    "first_assent_date": date(1786, 4, 8) # date is another type we will get to later
    "first_assent_party": ["Jacques Balmat", "Michel-Gabriel Paccard"]
}

# And many more...
# You can even make your own
```

There is one confusing things about types and only because its not obvious. There are two types of data types, value types and reference types.
Strings, ints, floats, bools, dates are value types while lists dicts ands classes are reference types.

To explain the difference between value types and reference types lets go back to our man at the memory counter.
If we ask him to store our keys, he just puts them in a box on a shelf behind him,
If we ask him to store our entire car its a lot of work to try get that on a shelf so instead he parks in round the back in parking bay, takes a photo of your car, writes where he parked it on the photo then puts that photo in a box on his shelf.
When you ask for your car back he just gives you the photo.
Here the car and photo is a reference type (the photo is the reference) and the key is a value type.
So with value types you just get the thing you stored back but with reference types you get a reference to the thing back.
Reference types are generally for large things and value types are for small things.
We will cover why is matters soon.
This metaphor also starts to breakdown a little here, to python the photo(reference) of the car is more like a portal to the car, you can use the car through its photo (reference) which does not make sense in our world.

## Recap

So far we have learn that:

- We can store data in memory by assigning data to a variable.
- Each bit of data has a specific type, like a string, int or dict.
- There two catagories of types, value and reference types.

Python is a popular high-level, dynamically typed, and interpreted language.

- hig-level: (also called managed or garbage collected) Python automatically deletes unused memory so we don't have to concern ourselves with low level memory management. (the bit of python that does this is called the garbage collector)
- dynamically typed: A python variable can be assigned one type and then later a different type and it automatically adjusts.
- interpreted: Python code in run by an interpreter and executed the instructions as it reads them.

## Next

We will actually write a "useful" program

---

## Scrap

```py
class Bicycle():
    def __init(self, name:str, price:float, is_sold:bool = False):
        self.name = name
        self.price = price
        self.is_sold = is_sold

stock = [
        Bicycle("Specialized", 200000),
        Bicycle("Santa Cruz ", 100000, True),
        Bicycle("FunctionsBianchi", 900000)
    ]

def sum_stock_value(bicycles: List[Bicycle]):
    total = 0
    for bike in bicycles:
        if not bike.is_sold:
            total = total + bike.price
    return total

current_stock_value = sum_stock_value(stock)
print(current_stock_value)

# Output: 1200000
```
