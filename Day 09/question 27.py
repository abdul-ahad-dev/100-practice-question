# Print first 25 prime numbers


# Define a function to check if a number is prime
def is_prime(n):
    i = 2
    # If the number is less than or equal to 1, it's not prime
    if n <= 1:
        return False
    # Iterate from 2 to half of the number
    while i <= n/2:
        # If the number is divisible by any number between 2 and half of the number, it's not prime
        if n % i == 0:
            return False
        i += 1
        # If the number passes all the checks, it's a prime number
    return True


# Main function to take user input and print prime number

def prime_number(end_numb):

    # Iterate over the range of integers end_num
    for num in range(0, end_numb+1):
        # check if prime number this code will execute
        if is_prime(num):
            # print prime number
            print(num)


# Main function to take user input and check if the number is prime
def main():
    while True:
        try:
            # Ask the user to enter a number
            user_input = int(input("Enter a number range to print prime number: "))
            break
        except ValueError:
            # Handle the case where the user enters a non-integer value
            print("Please enter a valid number!!!")

    # Call prime_number function
    prime_number(user_input)


# Execute the main function if the script is run directly
if __name__ == "__main__":
    main()
