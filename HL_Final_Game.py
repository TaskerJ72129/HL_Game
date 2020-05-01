import math
import random

print("welcome to the Higher Lower Game")
print()


# Number Checking function
def intcheck(question, low = None, high = None):

    # Set up error messages


    if low is not None and high is not None:
        error = "Please enter an integer between {} and {} (Inclusive)".format(low, high)
    elif low is not None and high is None:
        error = "Please enter an integer that is more than or equal to {}".format(low)
    elif low is None and high is not None:
        error = "Please enter an integer that is less than or equal to {}".format(high)
    else:
        error = "Please enter an integer"

    while True:

        try:
            response = int(input(question))

            # Checks response is not too low
            if low is not None and response < low:
                print(error)
                continue

            if high is not None and response > high:
                print(error)
                continue

            return response

        except ValueError:
            print(error)
            continue

# Main Routine

keep_going = ""
while keep_going == "":

    lowest = intcheck("Low Number: ")
    highest = intcheck("High Number: ", lowest + 1)

    range = highest - lowest + 1
    max_raw = math.log2(range)
    max_upped = math.ceil(max_raw)
    max_guesses = max_upped + 1

    print("")

    guesses_allowed = max_guesses
    rounds = intcheck("rounds: ")
    game_stats = []

    num_won = 0
    rounds_played = 0

    while rounds_played < rounds:
        secret = random.randint(lowest, highest)
        guess = ""
        guesses_left = guesses_allowed
        already_guessed = []

        print("Round {}".format(rounds_played + 1))

        while guess != secret and guesses_left >= 1:
            guess = intcheck("Guess: ")

            if guess in already_guessed:
                print("You already guessed that number! Please enter a different number")
                print("You still have {} guesses left".format(guesses_left))
                print()
                continue

            already_guessed.append(guess)
            guesses_left -= 1

            if guesses_left < 1:
                if guess != secret:
                    print("LOL, You lose")
                    print()
                    guesses_left -= 1
                    break
                else:
                    print("Well done! You guessed the secret number")
                    print("You got it on the final guess")
                    print()
                    num_won += 1
                    break

            elif guess == secret and guesses_left == (guesses_allowed - 1):
                print("EPIC, you got it first try!")
                print()
                num_won += 1

            else:
                if guess < secret:
                    print("Too low, try a higher number")
                    print("You still have {} guesses left".format(guesses_left))
                    print()

                elif guess > secret:
                    print("Too high, try a lower number")
                    print("You still have {} guesses left".format(guesses_left))
                    print()

                else:
                    num_won += 1
                    print()
                    print("Well done! You guessed the secret number")
                    if guesses_left == 1:
                        print("You had {} guess remaining".format(guesses_left))
                    else:
                        print("You had {} guesses remaining".format(guesses_left))

        game_stats.append(guesses_allowed - guesses_left)
        print("Won: {} \t | \t Lost: {}".format(num_won, rounds_played - num_won + 1))
        print()
        rounds_played += 1

    range = highest - lowest + 1
    max_raw = math.log2(range)
    max_upped = math.ceil(max_raw)
    max_guesses = max_upped + 1

    print()

    print("*** Game Scores ***")
    list_count = 1
    for item in game_stats:

        # Indicates if game has been won or lost
        if item <= guesses_allowed:
            status = "won"
        else:
            status = "lost"

        print("Round {}: {} ({})".format(list_count, item, status))
        list_count += 1

    # Calculate statistics
    game_stats.sort()
    best = game_stats[0]
    worst = game_stats[-1]
    average = sum(game_stats)/len(game_stats)

    print()
    print("***Summary Statistics***")
    print("Best: {}".format(best))
    print("Worst: {}".format(worst))
    print("Average: {:.2f}".format(average))


    print("Thanks for playing")
    print()
    keep_going = input("Press <enter> to play again or any key to quit: ")
    print()
