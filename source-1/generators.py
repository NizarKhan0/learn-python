# range(100)
# list(range(100)

# def make_list(num):
#     result = []
#     for i in range(num):
#         result.append(i)
#     return result

# my_list = make_list(100)
# print(my_list)
# print(list(range(1000)))

# Generators 2
# Iterable
# Iterate

def generator_function(num):
    for i in range(num):
        yield i * 2  # Yielding even numbers

g = generator_function(100)
next(g)  # This will get the first even number, which is 0
next(g)  # This will get the second even number, which is 2
print(next(g))  # This will print the first even number, which is 0
# print(g)  # This will print a generator object
# for item in generator_function(1000):
#     print(item)


# generators perfomance

from time import time
def perfomance(fn):

@perfomance
def long_time():
    print('1')
    for i in range(1000000):
        i * 5

@perfomance
def long_time2():
    print('2')
    for i in range(1000000):
        i * 5

long_time()
long_time2()

def gen_fun(num):
    for i in range(num):
        yield i

for item in gen_fun(100):
    print(item)