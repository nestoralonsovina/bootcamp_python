from random import randint

def main():
    print("This is an interactive guessing game!")
    print("You have to enter a number between 1 and 99 to find out the secret number.")
    print("Type 'exit' to end the game.")
    print("Good luck!")

    secret_number = randint(1, 99)
    tries = 0

    while True:

        print("What's your guess between 1 and 99?")
        guess = input(">> ")

        if guess == "exit":
            print("Goodbye!")
            break

        try:
            guess = int(guess)
        except ValueError:
            print("That's not a number.")
            continue

        if guess > secret_number:
            print("Too high!")
        elif guess < secret_number:
            print("Too low!")
        else:
            if secret_number == 42:
                print("The answer to the ultimate question of life, the universe and everything is 42.")
            if tries == 1:
                print("Congratulations! You got it on your first try!")
            else:
                print("Congratulations, you've got it!\nYou won in " + str(tries) + " attempts!")
            break


if __name__ == "__main__":
    main()