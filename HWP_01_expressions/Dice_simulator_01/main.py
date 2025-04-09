
import random

print("Welcome to dice roll simulator!")

die_sides = 6

def roll_dice():
    die1 : int = random.randint(1, die_sides)
    die2 : int = random.randint(1, die_sides)
    total : int = die1 + die2
    print(f"Total of the two dice: {total}")


def main():
    die1 : int = 10
    print(f"die1 in main() starts as {die1}")
    roll_dice()
    roll_dice()
    roll_dice()
    print(f"die1 in main() is still {die1}")
    print("Goodbye!")

if __name__ == "__main__":
    main()
