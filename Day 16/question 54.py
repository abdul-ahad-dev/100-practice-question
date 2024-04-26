"""
finding word in string.
"""


def find_word(string, word):

    i = 0
    count = 0

    while i < len(string):

        if string[i:i+len(word)] == word:
            count = count + 1

        i = i + 1

    return count


def main():

    user_string = "how,are you are"

    target_word = 'are'

    occurrences = find_word(user_string, target_word)

    print(f"The word '{target_word}' appears {occurrences} times in the string.")


if __name__ == "__main__":

    main()
