"""
Find the index position of a particular character in another string.
"""


def find_index(string, element):

    for index, char in enumerate(string):

        if char == element:
            return index

    return -1


def main():

    word = "hello, how are you"

    print(word)

    letter = 'a'

    index = find_index(word, letter)

    if index != -1:
        print(f"The index of '{letter}' in '{word}' is: {index}")
    else:
        print(f"The character '{letter}' is not found in '{word}'")


if __name__ == "__main__":

    main()
