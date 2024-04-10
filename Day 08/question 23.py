# Write a program that will take user input of (4 digits number) and check whether the number is narcissist number or not.

# Define a function to check if a number is a narcissistic number

def is_narcissistic_number(n):
    sum = 0
    # Iterate over each digit in the number
    for i in str(n):
        # Calculate the sum of each digit raised to the power of the number of digits in n
        sum = sum + int(i) ** len(str(n))
        # Check if the sum is equal to the original number
    return n == sum


# Main function to take user input and check if the number is narcissistic
def main():
    while True:
        try:
            # Ask the user to enter a number
            num = int(input("Enter a Number : "))
            break
        except ValueError:
            # Handle the case where the user enters a non-integer value
            print("Please enter a valid number")

    # Check if the entered number is narcissistic and print the result
    if is_narcissistic_number(num):
        print("Yes, This is narcissistic number")
    else:
        print("No, This is not narcissistic number")


# Execute the main function if the script is run directly
if __name__ == "__main__":
    main()