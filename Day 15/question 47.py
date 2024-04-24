"""
Count the frequency of a particular character in a provided string. Eg 'hello how are you' is the string, the frequency of h in this string is 2
"""


def string_count(a, s):
    count = 0

    for i in s:
        if a == i:
            count = count + 1

    return count


def main():
    message = 'hello how are you'

    alpha = string_count(a='h', s=message)

    print(message)
    
    print("the word alphabet 'h' in above string is: ", alpha)


if __name__ == "__main__":

    main()
