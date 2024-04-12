# User will provide 2 numbers you have to find the by LCM of those 2 numbers


def find_hcf(n1, n2):

    if n1 == 0 or n2 == 0:
        return 0

    while n2 != 0:
        remainder = n1 % n2
        n1 = n2
        n2 = remainder

    return n1


def find_lcm(a, b):
    product = a * b
    hcf = find_hcf(a, b)
    lcm = product // hcf
    return lcm


def main():
    while True:
        try:
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            break
        except ValueError:
            print("Enter valid number!!!")

    lcm = find_lcm(num1, num2)
    print("The Least Common Multiple (LCM) of", num1, "and", num2, "is", lcm)


if __name__ == "__main__":
    main()
