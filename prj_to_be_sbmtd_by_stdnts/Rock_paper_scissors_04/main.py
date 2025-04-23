
import random

def main():
    user_choice: str = input('What`s your choice: r for rock | p for paper | s for scissors : ')
    computers_choice: str = random.choice(['r', 'p', 's'])

    if user_choice == computers_choice:
        return 'The game is tied!'

    if win_lose(user_choice, computers_choice):
        return 'You Won!'

    return 'You Lose!'


def win_lose(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
    

if __name__ == '__main__':
    print(main())
