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