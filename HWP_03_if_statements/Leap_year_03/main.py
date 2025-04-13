

def main():
    print("This program checks if a year is a leap year or not.")
    print('')
    check_year : int = int(input("Enter a year to check if it is a leap year or not: "))
    if check_year % 4 == 0:
        if check_year % 100 == 0:
            if check_year % 400 == 0:
                print(f"{check_year} is a leap year.")
            else:
                print(f"{check_year} is not a leap year.")
        else:
            print(f"{check_year} is a leap year.")
    else:
        print(f"{check_year} is not a leap year.")

if __name__ == "__main__":
    main()
