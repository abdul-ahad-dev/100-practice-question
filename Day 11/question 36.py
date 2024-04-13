"""
Print all factors of a given number provided by the user.

"""

# Function to print all factors of a given number
def factors(n):
    # Iterate from 1 to n
    for i in range(1, n + 1):
        # Check if n is divisible by i
        if n % i == 0:
            # Print i as a factor of n
            print(i)


# Main function to get user input and handle exceptions
def main():
    # Infinite loop to keep asking for user input until a valid number is entered
    while True:
        try:
            # Get the number from the user
            num = int(input("Enter a number: "))
            # Break the loop if a valid number is entered
            break
        # Catch ValueError exception if user enters a non-integer value
        except ValueError:
            # Print error message
            print("Enter valid number!!!")

    # Call the factors function with the entered number as argument
    factors(num)


# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()
