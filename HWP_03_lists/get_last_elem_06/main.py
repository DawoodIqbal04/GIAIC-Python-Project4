def get_first_element(lst):
    if lst:
        print("First element:", lst[-1])
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
    lst = get_list()
    get_first_element(lst)

if __name__ == "__main__":
    main()
