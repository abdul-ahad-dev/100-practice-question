# Write a program that will give you the sum of 3 digits

def sum(n1, n2, n3):
    s = n1 + n2 + n3
    return s


if __name__ == '__main__':
    num1 = float(input("Enter first number : "))
    num2 = float(input("Enter second number : "))
    num3 = float(input("Enter Third number : "))

    sum = sum(num1, num2, num3)

    print(f"Sum of {num1} + {num2} + {num3} is = {sum}")
