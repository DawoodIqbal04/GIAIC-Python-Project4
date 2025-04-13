
VOTING_AGE_IN_SCOTLAND = 16
VOTING_AGE_IN_PAKISTAN = 18
VOTING_AGE_IN_KUWAIT = 21
VOTING_AGE_UNITED_ARAB_EMIRATES = 25

def main():
    print("🎉 Welcome to the voting age calculator!")

    age : int = int(input("Please enter your age: "))

    if age >= VOTING_AGE_IN_SCOTLAND:
        print(f"You are {age} and your are eligible to vote in Scotland! ✅")
    else:
        print(f"You are {age} and your are not eligible to vote in Scotland! ❌")

    if age >= VOTING_AGE_IN_PAKISTAN:
        print(f"You are {age} and your are eligible to vote in Pakistan! ✅")
    else:
        print(f"You are {age} and your are not eligible to vote in Pakistan! ❌")

    if age >= VOTING_AGE_IN_KUWAIT:
        print(f"You are {age} and your are eligible to vote in Kuwait! ✅")
    else:
        print(f"You are {age} and your are not eligible to vote in Kuwait! ❌")

    if age >= VOTING_AGE_UNITED_ARAB_EMIRATES:
        print(f"You are {age} and your are eligible to vote in United Arab Emirates! ✅")
    else:
        print(f"You are {age} and your are not eligible to vote in United Arab Emirates! ❌")

    if age > 25:
        print(f"You are {age} and your are eligible to vote in all countries of the world! ✅")
    elif age < VOTING_AGE_IN_SCOTLAND:
        print(f"You are {age} and your are not eligle to vote any country of the world: ❌")


if __name__ == "__main__":
    main()
