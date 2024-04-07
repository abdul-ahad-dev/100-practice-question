# Write a program to find the volume of the cylinder. Also find the cost when ,when the cost of 1litre milk is 40Rs.

import math


def cylinder_volume(radius, height):

    volume = math.pi * (radius ** 2) * height
    return volume


def milk_cost(volume):

    cost = volume * 40
    return cost


def main():
    while True:
        try:
            radius = float(input("Enter the radius of the cylinder: "))
            height = float(input("Enter the height of the cylinder: "))
            break
        except ValueError:
            print("Please enter valid numbers.")

    volume = cylinder_volume(radius, height)
    cost = milk_cost(volume)

    print(f"The volume of the cylinder is: {volume}")
    print(f"The cost of the given volume of milk is: {cost} Rs")


if __name__ == "__main__":
    main()
