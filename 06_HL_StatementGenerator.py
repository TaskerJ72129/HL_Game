# HL component 6 - Statement Generator

def hl_statement(statement, char):
    print()
    print(char*len(statement))
    print(statement)
    print(char*len(statement))
    print

# Main rountine

too_low = hl_statement("^^ Too low, try a higher number.    |   "
                       "Guesses Left: 3 ^^", "^")
print()
too_high = hl_statement("vv Too high, try a lower number.   |   "
                        "Guesses Left: 2 vv", "v")
print()
duplicate = hl_statement("!! You already guessed that number, Please try again  |   "
                         "Guesses left: 2 !!", "!")
print()
well_done = hl_statement("*** Well done! You got it in 3 guesses ***", "*")

print()
start_round = hl_statement("### Round 1 of 3 ###", "#")

print()
loss = hl_statement("--- You Lose ---", "-")

print()
first_try = hl_statement("$$$ EPIC, You got it first try $$$", "$")
