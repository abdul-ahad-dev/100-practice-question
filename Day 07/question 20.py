# Write a program to find the sum of first n numbers, where n will be provided by the user. Eg if the user provides n=10 the output should be 55.

def sum_of_first_n_numbers(n):

    sum = 0
    for i in range(n+1):
        sum += i

    return sum


def main():

    while True:
        try:
            n = int(input("Enter the value of n: "))
            break
        except ValueError:
            print("Please enter valid number")

    result = sum_of_first_n_numbers(n)

    print(f"The sum of the first {n} numbers is : {result}")


if __name__ == "__main__":
    main()
