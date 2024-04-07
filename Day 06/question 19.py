def sum_of_squares(number):
    sum = 0
    while number > 0:
        digit = number % 10
        sum += digit ** 2
        number = number // 10
    return sum


def main():
    while True:
        try:
            number = int(input("Enter a three-digit number: "))
            if 99 < number < 1000:
                break
            else:
                print("Please enter a valid three-digit number.")
        except ValueError:
            print("Please enter a valid number.")

    sum = sum_of_squares(number)
    print(f"The sum of the squares of each digit is {sum}.")


if __name__ == "__main__":
    main()
