# HL Component 5 - no duplicates

secret = 7
guesses_allowed = 5

already_guessed = []
guesses_left = guesses_allowed
num_won = 0

guess = ""

while guess != secret and guesses_left >= 1:
    guess = int(input("Guess: "))

    if guess in already_guessed:
        print("You already guessed that number! Please enter a different number")
        print("You still have {} guesses left".format(guesses_left))
        continue

    guesses_left -= 1
    already_guessed.append(guess)

    if guesses_left < 1:
        if guess != secret:
            print()
            print("LOL, you lose")
            break
        else:
            print()
            print("Well done! You guessed the secret number")
            print("You got it on the final guess")
            break

    elif guess == secret and guesses_left == (guesses_allowed - 1):
        print()
        print("EPIC! you got it first try!")

    else:
        if guess < secret:
            print("Too low, try a higher number")
            print("You still have {} guesses left".format(guesses_left))

        elif guess > secret:
            print("Too high, try a lower number")
            print("You still have {} guesses left".format(guesses_left))

        else:
            print()
            print("Well done! You guessed the secret number")
            if guesses_left == 1:
                print("You had {} guess remaining".format(guesses_left))
            else:
                print("You had {} guesses remaining".format(guesses_left))
            break

print("Thanks for playing")
