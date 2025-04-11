
def main():
    divident : int = int(input("Enter the number you want to be divided: "))
    divisor : int = int(input("Enter the number you want to divide with: "))
    result : int = divident // divisor
    remainder : int = divident % divisor

    print(f"The result of the division is {str(result)} and it's remainder is {str(remainder)}.")

if __name__ == "__main__":
    main()
