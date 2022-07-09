# 4. roundOff a float number having only one decimal place (3.2 = 3; 4.8 =5 etc) 
# Note: It is not allowed to use any inbuilt language function.

def roundOff(num):
    i = int(num)
    if num > i+0.5:
        return i + 1
    else:
        return i
        
user_input = 4.8
print("Input: ", user_input)
print("Output: ",roundOff(user_input))