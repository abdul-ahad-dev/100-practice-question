# Task
# The provided code stub reads two integers, a and b, from STDIN.
#
# Add logic to print two lines. The first line should contain the result of integer division, a // b. The second line should contain the result of float division,  / .
#
# No rounding or formatting is necessary.
import math


def check_num(num1, num2):
    print(f"the result of the integer division {num1}/{num2} = ", math.floor(num1/num2))
    print(f"the result of the integer division {num1}/{num2} = ", num1/num2)



if __name__ == '__main__':
    a = int(input())
    b = int(input())
    check_num(a, b)

