# import datetime
#perfomance decorator
from time import time
from array import array

# print(datetime.date.today())
# print(datetime.datetime.now().strftime("%H:%M:%S"))

# time
def performance(func):
    def wrapper(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()
        execution_time = end_time - start_time
        print(f"Function '{func.__name__}' executed in {execution_time:.4f} seconds")
        return result
    return wrapper

@performance
def long_time():
    for i in range(1000000):
        i * 5

long_time()

# array

arr = array('i', [1, 2, 3, 4, 5])
print(arr)
