# HL Component 3 - Compare user guess with secret number

secret = 7
guess = ""

while guess != secret:

    guess = int(input("Guess: "))

    if guess < secret:
        print("Too low, try a higher number")
    elif guess > secret:
        print("Too high, try a lower number")
    else:
        print("Well done! You guessed the secret number")
