def get_first_element(lst):
    if lst:
        print("First element:", lst[0])
    else:
        print("The list is empty.")

def get_list():
    lst = []
    while True:
        element = input("Enter an element of the list (or press Enter to finish): ")
        if element == "":
            break
        lst.append(element)
    return lst

def main():
    lst = get_list()  # Get the list from the user
    get_first_element(lst)  # Print the first element

if __name__ == "__main__":
    main()
