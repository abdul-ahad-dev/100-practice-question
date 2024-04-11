# Take a number from the user and find the number of digits in it.


# Define a function to count the number of digits in a given number
def check_numb_digit(n):
    count = 0
    # Loop until the number becomes 0
    while n > 0:
        # Get the last digit of the number
        digit = n % 10
        # Increment the count of digits
        count += 1
        # Remove the last digit from the number
        n = n // 10
    # Return the count of digits
    if count == 0:
        return 1
    return count


# Define the main function
def main():
    # Use a while loop to continuously prompt the user until a valid number is entered
    while True:
        try:
            # Get user input as an integer
            user_input = int(input("Enter a number: "))
            # Break out of the loop if a valid integer is entered
            break
        except ValueError:
            # Handle the ValueError exception if the user enters a non-integer value
            print("Enter valid number!!!")

    # Call the function to count the number of digits in the user input
    digit = check_numb_digit(user_input)
    # Print the result
    print("the number of digits is: ", digit)


# Check if the script is being run directly
if __name__ == "__main__":
    # Call the main function if the script is run directly
    main()
