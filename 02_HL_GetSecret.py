# HL Component 2 - Generates random number between low and high

import random

low = int(input("What is low? "))
high = int(input("What is high? "))

for item in range(1,20):
    secret = random.randint(low, high)
    print(secret, end = "\t")

