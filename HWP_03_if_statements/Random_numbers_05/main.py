
import random

number_size = 10
Min_value = 1
Max_value = 100

def main():
    random_numbers = [random.randint(Min_value, Max_value) for i in range(number_size)]
    print("Random numbers:", random_numbers)

if __name__ == "__main__":
    main()
