# Write a program that can find the factorial of a given number provided by the user.

def factorial(n):
    if n != 0:
        return factorial(n-1) * n
    else:
        return 1


def main():
    while True:
        try:
            n = int(input("Enter a number : "))
            break
        except ValueError:
            print("please enter a valid number")

    result = factorial(n)
    print(f"Factorial of {n} is : {result}")


if __name__ == "__main__":
    main()
