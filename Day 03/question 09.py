# Write a program that will reverse a four-digit number. Also, it checks whether the reverse is true

def reversed_num(n):
    reverse = int(str(n)[::-1])
    return reverse


def palindrome(n):
    return n == reversed_num(n)


def main():
    try:
        num = int(input("Enter number four digits: "))
        if len(str(num)) != 4:
            print("Please enter a four digits number!")
            return

        reverse = reversed_num(num)
        if palindrome(num):
            print("This is a palindrome")
        else:
            print("This is NOT a palindrome")

    except ValueError:
        print("Please enter a valid number!!!")


if __name__ == "__main__":
    main()
