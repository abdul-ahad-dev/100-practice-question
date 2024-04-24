"""
Write a program which can remove a particular character from a string.
"""


def remove_element(remove_char, input_string):
    string = ''

    for char in input_string:

        if char != remove_char:

            string += char

    return string


def main():

    inp = "hello, how are you!"

    print(inp)

    remove_char = input("What element did you remove: ")

    after_remove = remove_element(remove_char, inp)

    print(after_remove)


if __name__ == "__main__":

    main()
