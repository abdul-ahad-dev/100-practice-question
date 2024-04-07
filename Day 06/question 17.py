# Write  a program that will tell whether the given number is divisible by 3 & 6.

def is_div_3_and_6(n):
    if n % 3 == 0:
        return True
    else:
        return False


def main():
    while True:
        try:
            user_input = int(input("Enter a number: "))
            break
        except ValueError:
            print("Please enter valid number")

    if is_div_3_and_6(user_input):
        print("Number is divisible by 3 & 6")
    else:
        print("Number is not divisible by 3 & 6")


if __name__ == "__main__":
    main()
