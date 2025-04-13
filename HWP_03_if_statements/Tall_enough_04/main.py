
MINIMUM_HIEGHT : float = 4.10

def main():
    your_height : float = float(input("Enter your height in Foot.Inches e.g. 3.11: "))
    if your_height >= MINIMUM_HIEGHT:
        print("You are tall enough to ride the roller coaster.")
    elif your_height >= 3.0 and your_height < MINIMUM_HIEGHT:
        print("You are not tall enough to ride the roller coaster. Maybe next year you can.")
    else: 
        print("You are not tall enough to ride the roller coaster. But you can try bumper cars.")

if __name__ == "__main__":
    main()
