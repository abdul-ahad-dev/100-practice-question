def natural_log(x):
    sum = 0
    for i in range(1, 8):
        if i == 1:
            term = (x - 1) / x
        else:
            term = (1/2) * pow(((x - 1) / x), i)
        sum = sum + term
    return sum


def main():
    while True:
        try:
            user_input = int(input("Enter a value of to calculate natural log: "))
            break
        except ValueError:
            print("Enter valid number!!!")

    result = natural_log(user_input)

    print(f"natural logarithm of {user_input} is: ", end='')
    print(result)


if __name__ == "__main__":
    main()
