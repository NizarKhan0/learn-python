import random
# import random as oulala

# print(dir(random))
print(random.randint(1, 10))
print(random.choice(['apple', 'banana', 'cherry']))

my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)
print(my_list)

# my_list = [1, 2, 3, 4, 5]
# oulala.shuffle(my_list)
# print(my_list)