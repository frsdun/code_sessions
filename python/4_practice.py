# 1. Print the words Hello world to the console
# 2. Define a variable and print that to the console
# 3. Define two integers, add them together and store the result, print the result
# 4. Define a function that takes no arguments and prints something to the console when called
# 5. Define a function that takes two arguments, adds them together and returns the result
# 6. Define a function that squares any number
# 7. Define or modify an existing function to add type hints to both the arguments and return types
# 8. Define a list of words
# 9. Loop through the list of words and print each word
# 10. Define a function that takes a list of words and makes them into a single string
# 11. Split a string by the space ( ) character
# 12. Change the case of a string
# 13. Reverse a list of words
# 14. Join a list of strings together without using a custom function


# 1
print("Hello world")

# 2
some_var = 5
print(some_var)

# 3
a = 1
b = 2
result = a + b
print(result)


# 4
def some_function():
    print("some thing")


some_function()


# 5
def add(a: int, b: int):
    answer = a + b
    return answer


x = add(1, 2)


# 6
def square_num(num: int) -> int:
    return num * num


y = square_num(2)

# # 8
words = ["one", "two", "three"]

# # 9
for word in words:
    print(word)


# 10
def words_to_sentence(words):
    sentence = ""
    for word in words:
        sentence = sentence + " " + word
    return sentence


words_to_sentence(words)

# 11
words = "three two one".split(" ")

# 12
print("some string".upper())

# 13
numbers = [3, 4, 5, 6]
numbers.reverse()
print(numbers)


# 14
def join_words_into_sentence(words):
    sentence = "... ".join(words)
    return sentence


sentence = join_words_into_sentence(["This", "was", "fun", "I", "hope"])
print(sentence)
