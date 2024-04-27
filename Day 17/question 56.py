"""
Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.


Example 1:

Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Example 2:

Input: s = "Mr Ding"
Output: "rM gniD"
"""


def reverse(w):

    words = w.split()

    reversed_words = [word[::-1] for word in words]

    reversed_sentence = ' '.join(reversed_words)

    return reversed_sentence


def main():

    print("Example: 1")

    s = "Let's take LeetCode contest"
    print(s)

    s = reverse(s)
    print(s)

    print()
    print("Example: 2")

    s = "Mr Ding"
    print(s)

    s = reverse(s)
    print(s)


if __name__ == "__main__":

    main()
