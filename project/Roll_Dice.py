import random

min = 1
max = 6

roll_again = "yes"

while roll_again == "yes" or roll_again == "y":
    print("Rolling dice...")
    print("The Values is: ", random.randint(min, max))

    roll_again = input("Roll Dice again? (y/n) \n")
