
C : int = 299792458

def main():
    mass_in_kg : float = float(input("Enter mass in kg: "))
    energy_in_joules : float = mass_in_kg * (C**2)

    print("e = mc^2")
    print(f"Mass is equal to {str(mass_in_kg)} kg")
    print(f"The speend of light is {str(C)} m/s")

    print(f"Energy is equal to {str(energy_in_joules)} Joules")

if __name__ == "__main__":
    main()
