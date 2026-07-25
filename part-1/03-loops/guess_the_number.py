from random import randint

def main() -> None:
    # Generate random number between 1 and 20
    secret_number = randint(1, 20)
    guess = None
    guesses_taken = 0

    print("I am thinking of a number between 1 and 20.")

    # Ask the player to guess 6 times
    for guesses_taken in range(1, 7):
        print("Take a guess.")
        guess = int(input("> "))

        if guess < secret_number:
            print("Your guess is too low.")
        elif guess > secret_number:
            print("Your guess is too high")
        else:
            break

    if guess == secret_number:
        print(f"Good job! You got it in {guesses_taken} guesses!")
    else:
        print(f"Nope. The number was {secret_number}")


if __name__ == "__main__":
    main()
