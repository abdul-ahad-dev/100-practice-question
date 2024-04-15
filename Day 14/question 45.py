"""
Write  a program to print the following pattern
        *
      * * *
    * * * * *
   * * * * * * *
* * * * * * * * *

"""


class PyramidPattern:
    @staticmethod
    def asterisk(n):
        for i in range(1, n+1):
            for j in range(n - i):
                print("  ", end='')
            for k in range(1, 2*i):
                print("* ", end='')
            print()

    @staticmethod
    def number(n):
        for i in range(1, n+1):
            for j in range(n - i):
                print("  ", end='')
            for k in range(1, 2 * i):
                print(i, "", end='')
            print()

    @staticmethod
    def alphabet(n):
        aplha = 65
        for i in range(1, n+1):
            for j in range(n - i):
                print("  ", end='')
            for k in range(i):
                print(chr(aplha), "  ", end='')
                aplha += 1
            print()
            aplha = 65


def main():
    while True:
        try:
            no_of_line = int(input("enter of line: "))
            break
        except ValueError:
            print("Enter valid number!!!")

    triangle = PyramidPattern()
    triangle.asterisk(no_of_line)
    print()
    triangle.number(no_of_line)
    print()
    triangle.alphabet(no_of_line)


if __name__ == "__main__":
    main()