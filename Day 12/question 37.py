"""
Write a program to calculate the sum of the following series till the nth term
1/1! + 2/2! + 3/3! + 4/4! +…….+ n/n!
n will be provided by the user
"""


def fact(numb):
    if numb == 1 or numb == 0:
        return 1
    return numb - fact(numb - 1)


def series(n):
    sum=0
    for i in range(1, n+1):
        term = i / fact(i)
        sum = sum + term
    return sum


def main():
    while True:
        try:
            user_input = int(input("Enter a number of term: "))
            break
        except ValueError:
            print("Enter valid number!!!")

    result = series(user_input)

    for i in range(1, user_input + 1):
        if i < user_input:
            print(f"{i}/{i}! + ", end='')
        else:
            print(f"{i}/{i}!.")

    print("Answer of above equation is: ")
    print(result)


if __name__ == "__main__":
    main()
