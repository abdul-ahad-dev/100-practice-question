# User will input (2 numbers).Write a program to swap the numbers

num1 = int(input("Enter frist number : "))
num2 = int(input("Enter second number : "))

print("Value before swapping is ", num1," and ", num2)

temp = num1
num1 = num2
num2 = temp

print("Value After swapping is ", num1," and ", num2)
