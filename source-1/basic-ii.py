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
