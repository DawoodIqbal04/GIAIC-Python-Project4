
max_length : str = 3

def shorten(lst):
    while len(lst) > max_length:
        last_elem = lst.pop()
        print(last_elem)

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
    shorten(lst)

if __name__ == "__main__":
    main()
