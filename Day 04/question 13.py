# Write a program that take a user input of three angles and will find out whether it can form a triangle or not.

def is_triangle(a1, a2, a3):
    if (a1 + a2 + a3) == 180:
        return True
    else:
        return False


def main():
    try:
        angle1 = float(input("Enter first angle: "))
        angle2 = float(input("Enter second angle: "))
        angle3 = float(input("Enter third angle: "))

        if is_triangle(angle1, angle2, angle3):
            print("This angle can form a triangle")
        else:
            print("This angle cannot form a triangle")

    except ValueError:
        print("Please enter valid angle!!")


if __name__ == "__main__":
    main()
