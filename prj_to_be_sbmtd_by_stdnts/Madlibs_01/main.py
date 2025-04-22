
adj: str = input('Enter adjective: ')
verb1: str = input('Enter verb: ')
verb2: str = input('Enter verb: ')
fav_personality: str = input('Enter your favorite personality: ')


def main():
    print('Welcome to the MadLibs Game, Enter The Belows: ')
    madlib: str = f'Frontend engineering is so {adj} because it feels like i am {verb1} in the {verb2}. And my favorite personality is {fav_personality}. '
    print(madlib)


if __name__ == "__main__":
    main()
