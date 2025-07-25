# Intro
def hello(func):
    func()


def greet():
    print("Hello, World!")


a = hello(greet)

print(a)

# @decorator
# def hello():
#     print("Hello, World!")


# Highest order functions

# def greet(func):
#     func()

# map(), filter(), reduce()
# Z


# Decorators
# def hello():
#     print("Hello, World!")

def my_decorator(func):
    def wrap_func():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrap_func


# @my_decorator
def hellod():
    print("Hello, World!")
# hellod()


@my_decorator
def bye():
    print("Goodbye, World!")
bye()

# a = my_decorator(bye)
# a()

# my_decorator(bye)()


# decorators 3

def my_decorator2(func):
    def wrap_func(*args, **kwargs):
        func(*args, **kwargs)
    return wrap_func

@my_decorator2
def hello2(greeting, emoji=':)'):
    print(greeting, emoji)
    
hello2('Hello')


#Decorators

from time import time
def perfomance(fn):
    def wrap_func(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'took {t2 - t1} milliseconds')
        return result
    return wrap_func
@perfomance
def long_time():
    for i in range(1000000):
        i * 5
long_time()