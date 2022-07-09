# 2. Find number of occurrences of each number from the array Every number is in the range [0....100].
# Public void numberOfOccurences (int [] input){
# //write logic here
# }
# Note: expecting O(n) solution which means no sorting or nested loops allowed

def numberOfOccurences(input):
    occurrences = dict()
    for i in input:
        if i in occurrences:
            occurrences[i]+=1
        else:
            occurrences[i]=1
    return occurrences

user_input = [10,10,10,20,20,35,65,65,43,20,35,65,10]
print("Input: ",user_input)
print("Output:", numberOfOccurences(user_input))