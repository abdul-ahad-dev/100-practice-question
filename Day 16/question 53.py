"""
Write a program which can remove a particular character from a string
"""


def remove_character(string, char_to_remove):

    result = ""

    for char in string:

        if char != char_to_remove:
            result += char

    return result


def main():

    string = "hello, how are you!!!"

    char_to_remove = 'o'

    result_string = remove_character(string, char_to_remove)

    print("Original string:", string)

    print("After removing '" + char_to_remove + "' in above string")

    print("String after removing character:", result_string)


if __name__ == "__main__":

    main()
