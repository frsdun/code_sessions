# Functions and scope

Lets write our own function that says hello back to you.

```py
def say_hello(first_name:str, last_name:str):
    full_name = first_name + " " + last_name
    print("Hello " + name)

```

Here we have declare our first function, its called `say_hello`.
So far we have just declared it, we have not told the computer to actually run it.

```py
say_hello("Tim")
say_hello("Sally Jones")
```

This will output `Hello Tim` and `Hello Sally Jones`.

Let breakdown how we declared the function.
First the word `def` tells the interpreter we are declaring a function. the `def` key word expects the next key word to be the name of the function, so in this case `say_hello`.

A function can have parameters. Here our function has one parameter and it has a name of `name`.
The variable called name is part of the function now and can be used anywhere inside the function, but not outside of it.

To run a function we just say the name of the function and give it the parameters it needs.
If we wrote `say_hello()` with no name parameter the output will just be `Hello ` because we never assigned the name parameter to anything.
If we wrote `say_hello` nothing will happen, we have to add the brackets to tell the computer to run the function, sometimes called "call" the function or "evoke" thr function.
