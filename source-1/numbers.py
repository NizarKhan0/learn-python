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

# Escape Sequences

# \n, \t, \\, \', \"

weather = "It\'s a nice day \nwith a lot of sunshine"
print(weather)  # It's a nice day


# Formatted Strings

name = "Nizar"
age = 24
print(f"Hello, my name is {name} and I'm {age} years old.")
print('Hi '+ name + '. You are ' + str(age) + ' years old.')
print('Hi {}. You are {} years old.'.format(name, age))

# String index

selfish = 'me me me'
        #  01234567

print(selfish[0]) # m
# [start:stop]
print(selfish[0:2]) # me
# [start:stop:stepover]
print(selfish[0:2:5]) # m
print(selfish[-1]) # e start from the end

# Immutability

selfish = 100
print(selfish)  # 100

# Built in Functions -  Python string methods

greet = 'Hello'
print(len(greet))  # 5
print(greet[0:len(greet)])  # Hello
print(greet[0:len(greet):2])  # Hlo
print(greet[::-1])  # olleH


quote = 'to be or not to be'

print(quote.upper())  # TO BE OR NOT TO BE
print(quote.lower())  # to be or not to be
print(quote.title())  # To Be Or Not To Be
print(quote.capitalize())  # To be or not to be
print(quote.replace('be', 'me'))  # to me or not to me
print(quote.find('be'))  # 3
print(quote.count('be'))  # 2

# booleans

name = 'Nizar'
is_cool = True
print(f"Hi, my name is {name}. Am I cool? {is_cool}")
print(bool(0))  # False
print(bool(1))  # True

# Exercise Type Conversion

# name = 'Nizar'
# age = 24
# relationship_status = 'Single'

# relationship_status = 'In a relationship'

# print(relationship_status)

# birth_year = input('What year were you born? ')
# # print(type(birth_year))  # <class 'str'>
# # Convert the input to an integer
# age = 2025 - int(birth_year)
# print(f"You age is: {age}")


# Exercise password checker

# username = input('Enter your username? ')
# password = input('Enter your password? ')

# password_length = len(password)
# hidden_password = '*' * password_length  # Mask the password with asterisks

# print(f"Hello {username}, your password is {hidden_password} and it is {password_length} characters long.")


# List

li = [1, 2, 3, 4, 5]
li2 = ['a', 'b', 'c', 'd', 'e']
li3 = [1, 2, 3, 'a', 'b', 'c', True]

print(li)

# list slicing
shopping_list = ['milk', 'bread', 'eggs', 'butter']
# print(shopping_list[0])  # milk
# print(shopping_list[1:3])  # ['bread', 'eggs']

shopping_list[0] = 'milk'
new_list = shopping_list[:]  # copy the entire list
# new_list = shopping_list[0:3]  # ['bread', 'eggs', 'butter']
shopping_list[0] = 'cheese'  # Change the first item to 'cheese'
print(shopping_list)  # ['cheese', 'bread', 'eggs', 'butter']
print(new_list)  # ['milk', 'bread', 'eggs']

# Matrix

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[0][1])  # 2

# list method 1

basket = [1, 2, 3, 4, 5]

# adding items
basket.append(6)  # Add 6 to the end of the list
print(basket)  # [1, 2, 3, 4, 5, 6]

basket.insert(0, 0)  # Insert 0 at the beginning of the list
print(basket)  # [0, 1, 2, 3, 4, 5, 6]

basket.extend([7, 8, 9])  # Add multiple items to the end of the list
print(basket)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# removing items
basket.pop()  # Remove the last item from the list
print(basket)  # [0, 1, 2, 3, 4, 5, 6, 7, 8]

basket.remove(2)  # Remove the first occurrence of 2 from the list
print(basket)  # [0, 1, 3, 4, 5, 6, 7, 8]

basket.clear()  # Remove all items from the list
print(basket)  # []


# list method 2

basket = ['a', 'b', 'c', 'd', 'e', 'a']

print(basket.index('b'))
print('a' in basket)  # True
print('f' in basket)  # False

print(basket.count('a'))  # 2

# list method 3

basket = ['a', 'x', 'b', 'c', 'd', 'e']

basket.sort()  # Sort the list in ascending order
print(basket)  # ['a', 'b', 'c', 'd', 'e']

print(sorted(basket))  # ['a', 'b', 'c', 'd', 'e'] (returns a new sorted list)

basket.copy()  # Create a shallow copy of the list
print(basket)  # ['a', 'x', 'b', 'c', 'd', 'e']

basket.reverse()  # Reverse the order of the list
print(basket)  # ['e', 'd', 'c', 'b', 'x', 'a']


# Common list patterns

# print(basket[::-1])  # Reverse the list using slicing
# print(basket)

print(range(1, 10))  # Create a range object from 1 to 9
print(list(range(1, 10)))  # Create a range object from 1 to 9

# Join

sentence = '!'
new_sentence = sentence.join(['This', 'is', 'a', 'sentence.'])  # Join the list of words into a sentence
print(new_sentence)  # This is a new_sentence.

sentence = ' '.join(['This', 'is', 'a', 'sentence.'])  # Join the list of words into a sentence
print(sentence)  # This is a sentence.

# list unpacking

a, b, c, *other, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)  # 1
print(b)  # 2
print(c)  # 3
print(other)  # [4, 5, 6]
print(d)  # 9

# none

weapons = None  # Assign None to a variable
print(weapons)  # None