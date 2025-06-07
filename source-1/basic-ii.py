# Conditional Logic

is_old = True
is_licensed = True

if is_old and is_licensed:
    print("You are old enough to drive and you have a license!")
elif is_old and not is_licensed:
    print("You are old enough to drive but you do not have a license.")
else:
    print("You are not old enough to drive and you do not have a license.")


# Truthy & Falsy

is_old = bool(0)  # False
is_licensed = bool("test")  # True

print(is_old)  # False
print(is_licensed)  # True

username = "admin"
password = ""

if username and password:
    print("{username} is logged in!.".format(username=username))
elif username and not password:
    print("Please enter your username or password!")


# Ternary Operator

# condition_if_true if condition else condition_if_false
is_friend = False
can_message = "Message allowed!" if is_friend else "Message not allowed!"
print(can_message)

# short circuiting
is_Friend = True
is_User = True

print(is_Friend or is_User)  # True
print(is_Friend and is_User)  # True
print(is_Friend and not is_User)  # False

# Logical Operators
# <> == != < > <= >= and or not

print(5 > 2)  # True
print("a" == "b")  # False
print(not (True))  # False


is_magician = True
is_expert = False

# Conditional Logic for Magician and Expert Status
if is_magician and is_expert:
    print("You are a master magician!")
# check if magician AND not expert: "At least you're getting there..."
elif is_magician and not is_expert:
    print("At least you're getting there...")
# check if not magician: "You need magic powers to be a magician..."
elif not is_magician:
    print("You need magic powers to be a magician...")

# is vs ==

# 'is' checks for identity, '==' checks for equality
print(True == bool(1))  # True
print("1" == 1)  # False
print([] == 1)  # False
print(10 == 10.0)  # True
print([1, 2, 3] == [1, 2, 3])  # True

print(True is True)  # True
print(True is bool(1))  # True
print("1" is 1)  # False
print([] is 1)  # False
print(10 is 10.0)  # False
print([1, 2, 3] is [1, 2, 3])  # False


# For Loops

# Looping Through a String
for item in "Zero to Mastery":
    print(item)

# Looping Through a List
for item in [1, 2, 3, 4, 5]:
    print(item)

# The break statement
fruits = ["apple", "banana", "cherry", "grape"]
for x in fruits:
    if x == "cherry":
        break
    print(x)


for item in (1, 2, 3, 4, 5):
    for x in ["a", "b", "c"]:
        print(1, "c")

# The continue statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)


# Iterables - Lists, Strings, Tuples, Sets, Dictionaries
# iterate -> one by one check each item in the collection

user = {"name": "Nizar", "age": 24, "is_verified": True}

for key, value in user.items():
    print(f"{key}: {value}")

for item in user.items():
    print(item)

for item in user.values():
    print(item)

for item in user.keys():
    print(item)


# counter

my_List = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

counter = 0
for item in my_List:
    counter += item
print("Sum of items in my_List:", counter)


# range

print(range(0, 10))  # range(0, 10)
for item in range(0, 10, 2):
    print(item)

for _ in range(2):
    print(list(range(10)))


# enumerate
# Using enumerate to get index and value

for i, char in enumerate("Zero to Mastery"):
    print(i, char)

for i, char in enumerate(list(range(100))):
    if char == 50:
        print(f"index of 50 is: {i}")


# while loop - infinite loop example
# Using a while loop to print numbers from 0 to 4
i = 0
while i < 50:
    print(i)
    i += 1
else:
    print("Loop finished successfully!")

# for vs while loop
my_List = [1, 2, 3]
for item in my_List:
    print(item)

i = 0
while i < len(my_List):
    print(my_List[i])
    i += 1

# while True:
#     response = input("Say something: ")
#     if response == "bye":
#         break  # This will create an infinite loop until you break it manually


# break
# Using break to exit a loop when a condition is met
for i in range(10):
    if i == 5:
        break  # Exit the loop when i is 5
    print(i)

# continue
# Using continue to skip the current iteration when a condition is met
for i in range(10):
    if i % 2 == 0:
        continue  # Skip even numbers
    print(i)  # This will only print odd numbers

# pass
# Using pass to do nothing in a loop when a condition is met
for i in range(10):
    if i == 5:
        pass  # Do nothing when i is 5
    print(i)  # This will print all numbers from 0 to 9, including 5


# GUI

# Exercise

picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 1, 1, 1, 1, 1, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
]

# if 0 - print ''
# if 1 - print *
# # 1 iterate over the picture
for row in picture:
    # 2 iterate over each item in the image
    for pixel in row:
        if pixel == 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()  # Print a new line after each row


# clean
# readability
# predictability
# DRY - Don't Repeat Yourself


fill = "$"  # Character to fill for 1
empty = " "  # Character to fill for 0

# 1 iterate over the picture
for row in picture:
    # 2 iterate over each item in the image
    for pixel in row:
        if pixel:
            print(fill, end=""),
            print(fill, end=""),
            print(fill, end=""),
        else:
            print(empty, end="")
            print(empty, end="")
    print()  # Print a new line after each row


# Exercise find duplicate

some_List = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 6, 8]

# Find duplicates in a list
# Using a loop to find duplicates in some_List
duplicates = []
for value in some_List:
    if some_List.count(value) > 1:
        # Check if the value is not already in the duplicates list
        # to avoid adding it multiple times
        if value not in duplicates:
            # Append the value to the duplicates list
            # if it is not already in the list
            duplicates.append(value)
print(duplicates)


# Functions


def say_hello():
    print("Hello, World!")


# Calling the function
say_hello()


def show_tree():
    for image in picture:
        for pixel in image:
            if pixel == 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()


# Calling the function
show_tree()
show_tree()
show_tree()

print(show_tree)


# Parameters and Arguments


# parameters
# Parameters are variables that are defined in the function signature
# Arguments are the values that are passed to the function when it is called


# Default Parameters
def say_hello_to(name="Mimi", emoji="😊"):
    # Default values for parameters
    print(f"Hello {name} {emoji}")


def say_hello(name, emoji):
    print(f"Ni hao {name} {emoji}")


# positional arguments
say_hello("Nizar", "😊")
say_hello("Alice", "👋")
say_hello("Xiao Ru", "🌟")

# keyword arguments
say_hello(emoji="😊", name="Nizar")
say_hello_to()


# return
def sum(num1, num2):
    def another_function(n1, n2):
        return n1 + n2

    return another_function(num1, num2)

    # not executed
    return 5
    print("hello")


# should do one thing realy well and return something

total = sum(10, 20)
print(total)  # 30

# print(sum(1, total))
# print(sum(10, sum(10, 5)))


# 1. Wrap the above code in a function called checkDriverAge(). Whenever you call this function, you will get prompted for age.


def checkDriverAge(age=0):  # Prompting for age

    # age = input("What is your age?: ")

    if int(age) < 18:
        return "Sorry, you are too young to drive this car. Powering off"
    elif int(age) > 18:
        return "Powering On. Enjoy the ride!"
    elif int(age) == 18:
        return "Congratulations on your first year of driving. Enjoy the ride!"


# Test calls (no input wrapping needed)
# print(checkDriverAge(92))  # Argument provided → "Powering On..."
# print(checkDriverAge())  # No argument → uses age=0 → "Sorry, you are too young..."


# Notice the benefit in having checkDriverAge() instead of copying and pasting the function everytime?

# 2 Instead of using the input(). Now, make the checkDriverAge() function accept an argument of age, so that if you enter:
# checkDriverAge(92);
# it returns "Powering On. Enjoy the ride!"
# also make it so that the default age is set to 0 if no argument is given.


# Method vs Functions
# A method is a function that is associated with an object. In Python, methods are functions that belong to an object (like a list or a string).
# list()
# print()
# max()
# min()
# input()


# A function is a block of code that performs a specific task and can be called independently.
def greet(name):

    # pass/return
    print(f"Hello, {name}!")


greet("Nizar")  # This is a function call


print("hellloo".upper())  # This is a method call on the string object 'hellloo'


# Docstrings - add comments & definitions to functions


def test(a):
    """
    Info: this function tests and prints parameter a
    """

    print(a)


test("!!!!")
help(test)  # Displays the docstring of the function
print(test.__doc__)  # Accessing the docstring directly


# Clean Code
def is_even(num):

    # if num % 2 == 0:
    #     return True
    # elif num % 2 != 0:
    #     return False

    # if num % 2 == 0:
    #     return True
    # else:
    #     return False

    # if num % 2 == 0:
    #     return True
    # return False

    return num % 2 == 0  # Returns True if even, False if odd


print(is_even(50))
