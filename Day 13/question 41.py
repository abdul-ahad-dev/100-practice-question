"""
Write a program that accepts 2 numbers from the user a numerator and a denominator and then simplifies it
Eg if the num = 5, den = 15 the answer should be ⅓
Eg if the num = 6, den = 9 the answer should be ⅔
"""


def simplify_fraction(n, d):
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    gcd_value = gcd(n, d)
    simp_num = n // gcd_value
    simp_den = d // gcd_value

    return simp_num, simp_den


def main():
    while True:
        try:
            num = int(input("Enter the numerator: "))
            den = int(input("Enter the denominator: "))
            break
        except ValueError:
            print("Enter valid number")

    simp_num, simp_den = simplify_fraction(num, den)

    print(f"The simplified fraction is {simp_num}/{simp_den}")


if __name__ == "__main__":
    main()
