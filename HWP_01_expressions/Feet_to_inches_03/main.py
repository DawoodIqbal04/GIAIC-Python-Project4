
inches_in_foot : int = 12

def main():
    foot : float = float(input("Enter the number of foot: "))
    inches : int = foot * inches_in_foot
    print(f"{foot} foot is equal to {inches} inches")

if __name__ == "__main__":
    main()
