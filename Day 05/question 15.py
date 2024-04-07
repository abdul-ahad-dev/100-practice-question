# Write a program to find the simple interest when the value of principle, rate of interest and time period is given.

def calculate_simple_interest(principal, rate, time):
    
    interest = (principal * rate * time) / 100
    return interest


def main():
    while True:
        try:
            principal = float(input("Enter the principal amount: "))
            rate = float(input("Enter the rate of interest (in percentage): "))
            time = float(input("Enter the time period (in years): "))
            break
        except ValueError:
            print("Please enter valid numbers.")

    interest = calculate_simple_interest(principal, rate, time)

    print(f"The simple interest is: {interest}")


if __name__ == "__main__":
    main()
