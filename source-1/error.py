# print(1+True)

# Exception error
# print(1+'hello')

# # Syntax error
# def test():
#     1 + name

#     li = [1, 2, 3]
#     print(li[3])

#     di = {'a': 1, 'b': 2}
#     print(di['c'])  # KeyError
#     print(1 / 0)

# test()


#  Error Handling

while True:
    try:
        age = int(input("What is your age? "))
        # print(f"Your age is: {age}")
        10/age
    except ValueError:
        print("PLease enter a number")
    except ZeroDivisionError:
        print("Please enter age higher than 0")
    else:
        print("Thank you!")
        break