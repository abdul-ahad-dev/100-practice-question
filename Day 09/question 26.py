# Print all the armstrong numbers in the range of 100 to 1000


# Define a function to check if a number is a armstrong number

def is_armstrong_number(n):
    sum = 0
    # Iterate over each digit in the number
    for i in str(n):
        # Calculate the sum of each digit raised to the power of the number of digits in n
        sum = sum + int(i) ** len(str(n))
        # Check if the sum is equal to the original number
    return n == sum


# Define a function to print armstrong number

def armstrong_number(s, e):

    # Iterate over the range of integers from s to e, inclusive
    try:
        for num in range(s, e+1):
            if is_armstrong_number(num):
                print(num)
        # Handle any ValueError exceptions that may be raised
    except ValueError:
        print("Start and end values must be non-negative.")


# Main function to take user input and check if the number is narcissistic
def main():
    start_numb = 100
    end_numb = 1000
    print("Armstrong number between 100 to 1000:")

    # print armstrong number
    armstrong_number(start_numb, end_numb)


# Execute the main function if the script is run directly
if __name__ == "__main__":
    main()
