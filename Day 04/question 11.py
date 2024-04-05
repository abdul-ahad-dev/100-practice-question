# Write a program that will tell whether the given year is a leap year or not.

def leap_year(y):
    check = False
    if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
        check = True

    return check


def main():
    try:
        user_input = int(input("Enter year to check is leap year or not : "))
        if leap_year(user_input):
            print("This is leap year")
        else:
            print("This is not leap year")
    except ValueError:
        print("Please enter valid number")


if __name__ == "__main__":
    main()
