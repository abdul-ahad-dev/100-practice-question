# Write a program that will tell whether the number entered by the user is odd or even

def check_even(n):
    even = False
    if n % 2 == 0:
        even = True

    return even


def main():
    try:
        num = int(input("Enter a number : "))
        if check_even(num):
            print("This is EVEN Number.")
        else:
            print("This is ODD Number.")
    except ValueError:
        print("Please enter a valid number")


if __name__ == "__main__":
    main()