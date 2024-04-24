"""
Find the length of a given string without using the len() function.
"""


def length(string):
    count = 0

    for i in string:
        count = count + 1

    return count


def main():
    name = "Abdul ahad"

    name_len = length(name)

    print(name_len)


if __name__ == "__main__":

    main()
