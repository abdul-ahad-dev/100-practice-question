# Write a program to print whether a given number is prime number or not


# Define a function to check if a number is prime
def is_palindrome(n):
    return n == n[::-1]


# Main function to take user input and check if the number is prime
def main():
    # Ask the user to enter a number
    num = input("Enter a string : ")

    # Check if the entered number is prime and print the result
    if is_palindrome(num):
        print("Yes, This is a palindrome")
    else:
        print("No, This is not a palindrome")


# Execute the main function if the script is run directly
if __name__ == "__main__":
    main()
