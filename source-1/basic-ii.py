# Conditional Logic

is_old = True
is_licensed = True

if is_old and is_licensed:
    print("You are old enough to drive and you have a license!")
elif is_old and not is_licensed:
    print("You are old enough to drive but you do not have a license.")
else:
    print("You are not old enough to drive and you do not have a license.")
