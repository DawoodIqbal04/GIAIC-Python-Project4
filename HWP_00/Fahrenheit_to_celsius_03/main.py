print("Fahrenheit to Celsius Convertor 🔥🌡")


def main():
    fahrenheit : str = input("Enter temperature in Fahrenheit: ")
    fahrenheit: int = int(fahrenheit)
    celsius : int = (fahrenheit - 32) * 5.0 / 9.0
    print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")


if __name__ == "__main__":
    main()
