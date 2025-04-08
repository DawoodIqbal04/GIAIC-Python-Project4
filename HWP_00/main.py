print("Simple two numbers sum calculator 🧮")


def main():
    num1 : str = input("Enter the first number: ")
    num1 : int = int(num1)
    num2 : str = input("Enter the second number: ")
    num2 : int = int(num2)
    sum : int = num1 + num2
    print("The sum of the numbers is " + str(sum) + ".")

if __name__ == "__main__":
    main()
