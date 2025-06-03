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
