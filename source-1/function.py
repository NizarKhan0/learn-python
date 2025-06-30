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
