# 1. Write an algorithm to reverse a character array. Method signature: public char [] reverse (char [] input).
# Note:
# 1.It is not allowed to use any inbuilt language function 
# 2.It is not allowed to use any temporary array
# 3.Basically it should be an in place reversal

def reverse(input):
    start = 0
    end = len(input)-1
    while start < end:
        temp = input[start]
        input[start] = input[end]
        input[end] = temp
        start+=1
        end-=1
    return input

user_input = "praditi"
print("Input: ",list(user_input))
print("Output: ",reverse(list(user_input)))