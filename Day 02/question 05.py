# User will input (3 Number).Find the greater one

a = int(input("Enter First Integer : "))
b = int(input("Enter Second Integer : "))
c = int(input("Enter Third Integer : "))

if a > b and a > c:
    print("First Number is greater")
elif b > a and b > c:
    print("Second Number is greater")
else:
    print("Third Number is greater")
