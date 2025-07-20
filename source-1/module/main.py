# import utility
from utility import multiply, divide
# from shopping.more_shopping.shopping_cart import buy
from shopping.more_shopping import shopping_cart

# print(utility.multiply(3, 4))  # Output: 12
# print(utility.divide(10, 2))  # Output: 5.0

# print(shopping.shopping_cart.buy("apple"))  # Output: ['apple']

# print(buy("apple"))
# Using the imported functions
print(shopping_cart.buy("apple"))  # Output: ['apple']

print(divide(10, 2))  # Output: 2.5
print(multiply(3, 4))  # Output: 12

# print(max[1, 2, 3])