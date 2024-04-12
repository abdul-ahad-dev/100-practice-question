# User will provide 2 numbers you have to find the HCF of those 2 numbers


def find_hcf(n1, n2):

    if n1 == 0 or n2 == 0:
        return 0

    while n2 != 0:
        remainder = n1 % n2
        n1 = n2
        n2 = remainder

    return n1


def main():
    while True:
        try:
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            break
        except ValueError:
            print("Enter valid number!!!")

    find_hcf(num1, num2)
    hcf = find_hcf(num1, num2)
    print("The HCF of", num1, "and", num2, "is", hcf)


if __name__ == "__main__":
    main()
