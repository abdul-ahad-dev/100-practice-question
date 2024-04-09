# Write a program to print the first 25 odd numbers

def main():
    print("First 25 odd numbers: ")
    number = 0
    count = 1
    while count <= 25:
        if number % 2 != 0:
            print(number)
            count += 1
        number += 1


if __name__ == "__main__":
    main()