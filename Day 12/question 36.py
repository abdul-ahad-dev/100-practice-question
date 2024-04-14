"""
Write a program that keeps on accepting a number from the user until the user enters Zero. Display the sum and average of all the numbers.
"""

sum = 0
count = 0
series = []

while True:
    try:
        user_input = int(input("Enter number: "))
        if user_input == 0:
            break

    except ValueError:
        print("enter valid number!!!")

    count = count + 1
    series.append(user_input)
    sum = sum + user_input

print(series)
print("sum of above series is: ", sum)
print("average of above series is: ", sum/count)
