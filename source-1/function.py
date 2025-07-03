# Pure function

# def multiply_by2(li):
#     new_list = []
#     for item in li:
#         new_list.append(item * 2)
#     return new_list

# print(multiply_by2([1, 2, 3]))

#  Mapping function

my_list = [1, 2, 3]
def multiply_by2(item):
    return item * 2

print(list(map(multiply_by2, my_list)))
print(my_list)

# Filter function

my_list2 = [1, 2, 3]
def check_odd(item):
    return item % 2 != 0

print(list(filter(check_odd, my_list2)))
print(my_list2)


# Zip Function

my_list3 = [1, 2, 3]
you_list = [10, 20, 30]
their_list = [100, 200, 300]

print(list(zip(my_list3, you_list, their_list)))
print(my_list3)


# Reduce Function

from functools import reduce

my_list4 = [1, 2, 3]

def accumulator(acc, item):
    print(acc, item)
    return acc + item

print(reduce(accumulator, my_list4, 0))
print(my_list4)


# Lambda Expressions
# lambda param: action(param)
my_list5 = [1, 2, 3]

print(reduce(lambda acc, item: acc + item, my_list5, 0))
print(my_list5)

# Exercise Lambda Expressions
# Square
my_list6 = [5, 4, 3]

print(list(map(lambda item: item * 2, my_list6)))

# List Sorting
a = [(0, 2), (4, 3), (9, 9), (10, -1)]
print(sorted(a, key=lambda item: item[1]))

# List Comprehensions (list, set, dictionary)

# list
my_list7 = [char for char in 'hello']
my_list8 = [num for  num in range(0, 100)]
my_list9 = [num**2 for num in range(0, 100)]
my_list10 = [num**2 for num in range(0, 100) if num % 2 == 0]

print(my_list7)
print(my_list8)
print(my_list9)
print(my_list10)

# set

simple_dict = {
    'a': 1,
    'b': 2,
    'c': 3
}

# my_dict = {key:value**2 for key, value in enumerate(range(0, 100)) if value % 2 == 0}
my_dict = {key: value**2 for key, value in simple_dict.items() if value % 2 == 0}

my_dict2 = {num: num*2 for num in [1, 2, 3]}

print(my_dict)
print(my_dict2)


# exercise

# standart method
some_list = ['a', 'b', 'c', 'd', 'b', 'm', 'n', 'n']

duplicates = []
for item in some_list:
    if some_list.count(item) > 1 and item not in duplicates:
        duplicates.append(item)

print(duplicates)

# list comprehension method

duplicates2 = list(set([x for x in some_list if some_list.count(x) > 1]))
print(duplicates2)