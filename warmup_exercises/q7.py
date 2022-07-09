# 7. Given two sorted arrays in ascending order , write a function which takes both as input and returns an array of common elements .
# A = [1,3,4,6,7,9]
# B=[1,2,4,5,9,10] OutputArray:[1,,4,9]
# Note: Solution should be in O(n)

def commonElements(array1, array2):
    ptr1=0
    ptr2=0
    len1 = len(array1)
    len2 = len(array2)
    result = []
    while ptr1 < len1 and ptr2 < len2:
        if array1[ptr1]< array2[ptr2]:
            ptr1 += 1
        elif array2[ptr2] < array1[ptr1]:
            ptr2 += 1
        else:
            result += [array2[ptr2]]
            ptr2 += 1
            ptr1 += 1
    return result

user_array1 = [1,3,4,6,7,9]
user_array2 = [1,2,4,5,9,10]
print("Input: ",user_array1,", ",user_array2)
print("Output: ",commonElements(user_array1,user_array2))