# Intro
def hello(func):
    func()
    
def greet():
    print("Hello, World!")

a = hello(greet)

print(a)

@decorator
def hello():
    print("Hello, World!")
    

# Highest order functions

def greet(func):
    func()

# map(), filter(), reduce()
def greet2():
    def func():
        return 5
    return func