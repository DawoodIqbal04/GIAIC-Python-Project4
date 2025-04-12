
def add_numbers(numbers) -> int :
    total : int = 0
    for number in numbers:
        total += number
    return total

def main():
    numbers: list[int] = [3, 4, 2, 5, 6]
    result: int = add_numbers(numbers)
    print(f"The sum of the numbers in list is: {result}")

if __name__ == "__main__":
    main()
