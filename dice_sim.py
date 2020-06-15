#dice simulator 
#simulate a dice roll
    #press y to (re)roll
#number rolled must be random

import random as random

# x = random.randint(1,6)

# def dice_roll():

#     if input("Roll Dice?") == "y":
#         print(x)
#     else:
#         print("Try again")
    
# dice_roll()

x = "y"
# ^creates initial statement of x = y loop
while x == "y":
    number = random.randint(1,6)
    # ^resets number after each roll
    if number == 1:
        print("---------")
        print("|       |")
        print("|   1   |")
        print("|       |")
        print("---------")
    elif number == 2:
        print("---------")
        print("|       |")
        print("|   2   |")
        print("|       |")
        print("---------")
    elif number == 3:
        print("---------")
        print("|       |")
        print("|   3   |")
        print("|       |")
        print("---------")
    elif number == 4:
        print("---------")
        print("|       |")
        print("|   4   |")
        print("|       |")
        print("---------")
    elif number == 5:
        print("---------")
        print("|       |")
        print("|   5   |")
        print("|       |")
        print("---------")
    elif number == 6:
        print("---------")
        print("|       |")
        print("|   6   |")
        print("|       |")
        print("---------")
    x = input("y to roll again or n to stop")
    # ^allows for user to continue or stop loop