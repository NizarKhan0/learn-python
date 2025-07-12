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

# while True:
#     try:
#         age = int(input("What is your age? "))
#         # print(f"Your age is: {age}")
#         10/age
#     except ValueError:
#         print("PLease enter a number")
#     except ZeroDivisionError:
#         print("Please enter age higher than 0")
#     else:
#         print("Thank you!")
#         break


#  Error Handling 2

def sum(num1, num2):
    try:
        return num1 + num2
    except (TypeError, ZeroDivisionError) as err:
    # except TypeError as err:
        print(err)
        # print(f'Please enter a numbers {err}')
        # print(f'Please enter a number' + str(err))

print(sum('1', 2))  # This will raise a TypeError
# print(sum(1, 2))    # This will return 3

# Excerise Error Handling
# while True:
#     try:
#         age = int(input("What is your age? "))
#         10/age
#     except ValueError:
#         print("Please enter a valid number")
#         continue
#     except ZeroDivisionError:
#         print("Please enter an age higher than 0")
#         break
#     else:
#         print("Thank you!")
#         break
#     finally:
#         print('ok, we are done!')
#     print('This will always run')


# Error Handling 3
while True:
    try:
        age = int(input("What is your age? "))
        10/age
        # raise ValueError("hey cut it out")  # This will raise a ValueError
        raise Exception("hey cut it out")  # This will raise a ValueError
    except ZeroDivisionError:
        print("Please enter an age higher than 0")
        break
    else:
        print("Thank you!")
        break
    finally:
        print('ok, we are done!')
    print('This will always run')

