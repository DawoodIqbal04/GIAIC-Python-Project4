
SENTENCE_START: str = "Panaversity is fun. I learned to program and used Python to make my "

def main():
    adjective : str = str(input("Enter a Adjective word: "))
    noun : str = str(input("Enter a Noun word: "))
    verb : str = str(input("Enter a Verb word: "))

    print(SENTENCE_START + adjective + " " + noun + " " + verb + ".")

if __name__ == "__main__":
    main()
