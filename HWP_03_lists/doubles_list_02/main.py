
def main():
    numbers: list[int] = [29, 41, 77, 36, 52]
    for i in range(len(numbers)):
        index : int = numbers[i]
        numbers[i] = index * 2


    print(numbers)

if __name__ == "__main__":
    main()
