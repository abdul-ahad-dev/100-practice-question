# Task
# Given an integer, , perform the following conditional actions:
#
# If  is odd, print Weird
# If  is even and in the inclusive range of 2 to 5, print Not Weird
# If  is even and in the inclusive range of 6 to 20, print Weird
# If  is even and greater than 20, print Not Weird
def check(num):
    if num % 2 == 0:
        if 6 < num <= 20 or num < 2:
            print("Weird")
        else:
            print("Not Weird")
    else:
        print("Weird")


if __name__ == '__main__':
    n = int(input().strip())

    check(n)
