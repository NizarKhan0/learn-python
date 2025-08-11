import random

def run_guess(guess, answer):
    if 0 < guess < 10:
        if guess == answer:
            print("Congratulations! You guessed the number.")
            return True
    else:
        print("Wrong guess, try again.")
        return False
    """A simple number guessing game."""
# if __name__ == '__main__':
answer = random.randint(1, 10)
while True:
    try:
        guess = int(input("Guess a number between 1 and 10: "))
        if(run_guess(guess, answer)):
            break
    except ValueError:
        print("Please enter a valid number.")
        continue