# 6. Write a function that takes in an integer array and returns the item that occurs most often.
# int Most_frequent(inputArray [])
# If n is an input element in the array the possible values for n 1 ≤ n ≤ 100 Note: Solution should be in O(n)

def Most_frequent(input):
    occurrences = dict()
    for i in input:
        if i in occurrences:
            occurrences[i]+=1
        else:
            occurrences[i]=1
    maxkey = input[0]
    for i in occurrences:
        if occurrences[i]>occurrences[maxkey]:
            maxkey = i
    return maxkey

user_input = [10,10,10,20,20,35,65,65,43,20,35,65,10]
print("Input: ",user_input)
print("Output:", Most_frequent(user_input))