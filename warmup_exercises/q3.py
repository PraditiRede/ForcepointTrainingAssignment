# 3. Find first maximum and second maximum number from an integer array 
# Note : expecting O(n) solution which means no sorting or nested loops allowed

import sys
def first_and_second_max(input):
    max = -sys.maxsize - 1
    max2 = -sys.maxsize - 1
    for i in input:
        if i>max:
            max=i
        elif i>max2 and i!=max:
            max2=i
    print("First maximum number: ",max)
    print("Second maximum number: ",max2)

user_input = [23, 54, 87, 26, 47, 2, 74, 94, 73, 28, 47, 92, 9, 44]
print("Input: ",user_input)
first_and_second_max(user_input)