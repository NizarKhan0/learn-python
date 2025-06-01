# Conditional Logic

is_old = True
is_licensed = True

if is_old and is_licensed:
    print("You are old enough to drive and you have a license!")
elif is_old and not is_licensed:
    print("You are old enough to drive but you do not have a license.")
else:
    print("You are not old enough to drive and you do not have a license.")


# Truthy & Falsy

is_old = bool(0)  # False
is_licensed = bool("test")  # True

print(is_old)  # False
print(is_licensed)  # True

username = "admin"
password = ""

if username and password:
    print("{username} is logged in!.".format(username=username))
elif username and not password:
    print("Please enter your username or password!")
