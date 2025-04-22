
import random

min_num: int = 1
max_num: int = 11

def main():
    random_num = int(random.randint(min_num, max_num))
    user_guess: int = int(input("Enter A Number To Guess (1 to 10) : "))

    while user_guess != random_num:
        if user_guess == '':
            print("Empty or invalid input! Try Again!")
        else:
            print(f"Your Guess: {user_guess}")
            print("This Number Is A Wrong Guess!")
            print('')
            user_guess = int(input("Enter A Number To Guess (1 to 10) : "))
    
    print(f"Your Guess: {user_guess} Is Matched With Random Number: {random_num}")


if __name__ == "__main__":
    main()
