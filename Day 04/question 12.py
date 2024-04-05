# Write a program to find the Euclidean distance between two coordinates.

import math


def euclidean_distance(x1, y1, x2, y2):
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance


def main():
    try:
        x1 = float(input("Enter the x-coordinate of the first point: "))
        y1 = float(input("Enter the y-coordinate of the first point: "))

        x2 = float(input("Enter the x-coordinate of the second point: "))
        y2 = float(input("Enter the y-coordinate of the second point: "))

        distance = euclidean_distance(x1, y1, x2, y2)
        print("The Euclidean distance between two point is : ", distance)

    except ValueError:
        print("Please enter valid coordinate")


if __name__ == "__main__":
    main()
