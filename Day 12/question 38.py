"""
Write a Python Program to Find the Sum of the Series till the nth term:
1 + x^2/2 + x^3/3 + … x^n/n
n will be provided by the user
"""

import math


def series(x, nth):
    sum = 0
    for i in range(1, 1 + nth):
        if i == 1:
            term = 1
        else:
            term = pow(x, i) / i
        sum = sum + term
    return sum


def main():
    while True:
        try:
            value_of_x = int(input("enter value of x: "))
            num_of_term = int(input("Enter a number of term: "))
            break
        except ValueError:
            print("Enter valid number!!!")

    result = series(value_of_x, num_of_term)

    for i in range(1, num_of_term + 1):
        if i == 1:
            print("1 + ", end='')
        elif i < num_of_term:
            print(f"{value_of_x}^{i}/{i} + ", end='')
        else:
            print(f"{value_of_x}^{i}/{i}.")

    print("Answer of above equation is: ")
    print(result)


if __name__ == "__main__":
    main()
