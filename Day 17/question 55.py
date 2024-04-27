"""
Example 1:
Input: s = "hello"
Output: 13
Explanation:
The ASCII values of the characters in s are: 'h' = 104, 'e' = 101, 'l' = 108, 'o' = 111. So, the score of s would be |104 - 101| + |101 - 108| + |108 - 108| + |108 - 111| = 3 + 7 + 0 + 3 = 13.

Example 2:
Input: s = "zaz"
Output: 50
Explanation:
The ASCII values of the characters in s are: 'z' = 122, 'a' = 97. So, the score of s would be |122 - 97| + |97 - 122| = 25 + 25 = 50.
"""


def calculate_score(s):
    score = 0

    for i in range(len(s) - 1):
        score += abs(ord(s[i]) - ord(s[i + 1]))

    return score


def main():

    s1 = "hello"
    s2 = "zaz"

    score_s1 = calculate_score(s1)
    score_s2 = calculate_score(s2)

    print(f"Score of '{s1}' is: {score_s1}")
    print(f"Score of '{s2}' is: {score_s2}")


if __name__ == "__main__":

    main()
