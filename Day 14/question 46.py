"""
Write a program to print the following pattern
*
* *
* * *
* *
*
"""

"""
Write a program to print the following pattern
*
* *
* * *
* * * *
* * * * *
"""


class PatternTriangle:
    @staticmethod
    def asterisk(n):
        for i in range(1, n + 1):
            print("  " * (n - i) + "* " * ((i*2)-1))

        for i in range(n - 1, 0, -1):
            print("  " * (n - i) + "* " * ((i*2)-1))

    @staticmethod
    def number(n):
        for i in range(1, n + 1):
            print("  " * (n - i), end="")
            for j in range(1, i + 1):
                print(j, '', end="")
            for k in range(i - 1, 0, -1):
                print(k, '',end="")
            print()

        for i in range(n - 1, 0, -1):
            print("  " * (n - i), end="")
            for j in range(1, i + 1):
                print(j, '', end="")
            for j in range(i - 1, 0, -1):
                print(j, '', end="")
            print()

    @staticmethod
    def alphabet(n):
        for i in range(n):
            print("  " * (n - i - 1), end="")
            for j in range(i + 1):
                print(chr(65 + j), ' ', end=" ")
            print()

        for i in range(n - 2, -1, -1):
            print("  " * (n - i - 1), end="")
            for j in range(i + 1):
                print(chr(65 + j), ' ', end=" ")
            print()


def main():
    while True:
        try:
            no_of_line = int(input("enter of line: "))
            break
        except ValueError:
            print("Enter valid number!!!")

    triangle = PatternTriangle()
    triangle.asterisk(no_of_line)
    print()
    triangle.number(no_of_line)
    print()
    triangle.alphabet(no_of_line)


if __name__ == "__main__":
    main()
