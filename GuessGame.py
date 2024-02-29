import random


def guess_number():
    number = random.randint(1, 100)

    tries = 0

    print("Welcome to the Guess Game!")
    print("I have chosen a random number between 1 and 100.")

    while True:
        # Get User Input
        guess = int(input("Guess a number between 1 and 100: "))
        tries = tries + 1

        # We need to check if the number guess is right or correct
        if guess == number:
            print(f"Congratulations! You guessed the right number {number} in {tries} tries!")
            break
        elif guess < number:
            print("Your guess is too low! Try Again")
        else:
            print("Your guess is too high! Try Again")


if __name__ == "__main__":
    guess_number()
