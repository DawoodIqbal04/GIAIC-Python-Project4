
def add_data(my_list, data):
    for i in range(3):
        my_list.append(data)


def main():
    massege : str = str(input("Enter a massage to copy: "))
    my_list : list = []
    print("Before adding data: ", my_list)
    add_data(my_list, massege)
    print("After adding data: ", my_list)


if __name__ == "__main__":
    main()
