from random import randint

# Generate a number between 1-10
answer = randint(1, 10)

# import from user?

# check that input is a number 1-10
while True:
    try:
        print(answer)
        guess = int(input("Guess a number between 1 and 10: "))
        if 0 < guess < 11:
            # print('all good')
            if guess == answer:
                print("You guessed it!")
                break
        else:
            print("Please enter a valid number between 1 and 10.")
    except ValueError:
        print("Please enter a valid number between 1 and 10.")
        continue


# check if number is the right guess. Otherwise, prompt user to guess again
