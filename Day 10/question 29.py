# Print the first 20 numbers of a Fibonacci series

def fibonacci_number(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_number(n - 1) + fibonacci_number(n - 2)


def fibonacci_series(r):
    for num in range(r):
        print(fibonacci_number(num))


def main():
    while True:
        try:
            user_input = int(input("Enter number of range: "))
            break
        except ValueError:
            print("Enter valid number!!!")

    fibonacci_series(user_input)


if __name__ == "__main__":
    main()
