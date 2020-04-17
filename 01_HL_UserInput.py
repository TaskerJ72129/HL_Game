# HL - Get (and Check) user input

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
lowest = intcheck("Low Number: ")
highest = intcheck("High Number: ", lowest + 1)
rounds = intcheck("Rounds: ", 1)
guess = intcheck("Guess: ", lowest, highest)
