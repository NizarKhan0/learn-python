#This is a comment

"""
This is a comment
written in
more than just one line
"""
print("Hello, World!")

# Fundamental Data Types
# int and float

print(type(6))
print(type(2 - 4))
print(type(2 * 4))
print(type(2 / 4)) #0.5

print(type(20+1.1))
print(2 ** 3)
print(2 // 4)
print(2 % 4)

# math functions
print(abs(-2)) # 2
print(round(2.6)) # 3

bool
str
list
tuple
set
dict

# Classes -> custom types

# Specialized Data Types

None


# operator precedence

print(2 + 3 * 4) # 14
print((2 + 3) + 4 ** 4) # 81

# ()
# **

# operational bin() and complex

print(bin(10)) # 0b1010
print(int('0b1010', 2)) # 10

#Variables

# Legal variable names:

# myvar = "John"
# my_var = "John"
# _my_var = "John"
# myVar = "John"
# MYVAR = "John"
# myvar2 = "John"

user_iq = 190
print(user_iq)

a,b,c = 1, 2, 3
print(a)
print(b)
print(c)

# augemented assignment operator

some_value = 5
some_value = 5 + 2
some_value += 2  # This is the same as some_value = some_value + 2
some_value -= 2  # This is the same as some_value = some_value - 2

print(some_value)

#strings

print(type("Hello Mimizu!"))

username = "Mimizu"
password = '1234'
long_string = '''
WOW
O O
---
'''
print(long_string)

first_name = "Nizar"
last_name = "Khan"
full_name = first_name + " " + last_name
print(full_name)


# string concatenation
print('Hello ' + 'World!')  # Hello World!

# Type conversion

a = str(123)  # '123'
b = int(a)  # 123
c = type(b) # <class 'int'>
print(c)  # <class 'int'>

# print(type(str(123)))  # '123'
# print(type(int(str(123))))  # '123'