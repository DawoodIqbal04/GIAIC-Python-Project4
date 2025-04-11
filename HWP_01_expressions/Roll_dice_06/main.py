
import random

sides_of_dice = 6

def roll_dice():
    die1 : int = int(random.randint(1, sides_of_dice))
    die2 : int = int(random.randint(1, sides_of_dice))

    print(f"Die 1: {die1}")
    print(f"Die 2: {die2}")
    print(f"Total of dice: {die1 + die2}")

if __name__ == "__main__":
    roll_dice()
