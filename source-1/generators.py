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

# from time import time
# def perfomance(fn):

# @perfomance
# def long_time():
#     print('1')
#     for i in range(1000000):
#         i * 5

# @perfomance
# def long_time2():
#     print('2')
#     for i in range(1000000):
#         i * 5

# long_time()
# long_time2()

# def gen_fun(num):
#     for i in range(num):
#         yield i

# for item in gen_fun(100):
#     print(item)


# Under the hood of generators

def special_for(iterable):
    iterator = iter(iterable)  # Get an iterator from the iterable
    while True:
        try:
            print(iterator)
            # Print the current item and get the next(iterator)  # Get the next item from the iterator
            print(next(iterator))
        except StopIteration:
            break  # Stop the loop when StopIteration is raised


special_for([1, 2, 3, 4, 5])  # This will print each item in the list


class MyGen():
    current = 0
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __iter__(self):
        return self

    def __next__(self):
        if MyGen.current < self.last:
            num = MyGen.current
            MyGen.current += 1
            return num
        else:
            raise StopIteration

gen = MyGen(1, 10)
for i in gen:
    print(i)


# Fibonacci Numbers

def fibonacci(number):
    a = 0
    b = 1
    for i in range(number):
        yield a  # Yield the current Fibonacci number
        temp = a  # Store the current Fibonacci number
        a = b
        b = temp + b  # Update to the next Fibonacci number

for x in fibonacci(20):
    print(x)
    
def fibonacci2(number):
    a = 0
    b = 1
    result = []
    for i in range(number):
        result.append(a)  # Append the current Fibonacci number to the result list
        temp = a  # Store the current Fibonacci number
        a = b
        b = temp + b
    return result  # Return the list of Fibonacci numbers

print(fibonacci2(20))  # This will print the first 20 Fibonacci numbers as a list