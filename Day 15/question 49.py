"""
Count the number of vowels in a string provided by the user.
"""


def vowel_count(string):
    vowel = 0
    string = string.lower()

    for i in string:

        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':

            vowel = vowel + 1

    return vowel


def main():
    para = """
    Paragraphs are the building blocks of papers. Many students define paragraphs in terms of length: 
    a paragraph is a group of at least five sentences, a paragraph is half a page long, etc. 
    In reality, though, the unity and coherence of ideas among sentences is what constitutes a paragraph.
    """

    vowel = vowel_count(para)

    print(para)

    print()

    print("Number of vowel in above string is: ", vowel)


if __name__ == "__main__":

    main()
