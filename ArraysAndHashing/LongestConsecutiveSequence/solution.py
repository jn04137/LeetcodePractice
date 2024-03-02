from typing import List

# Code must be in O(n) time

# return the length of the longest consecutive element sequence

input = [100,4,200,1,3,2]
input2 = [0,3,7,2,5,8,4,6,0,1]

'''
Looking at the brute-force solution, maybe store the value as key and then the next
consecutive integer as the value.

Iterate through the hashmap afterwards.
Would be approximately O(2n) = O(n)
'''

def longestConsecutiveOptimal(nums: List[int]) -> int:
    memory = {}

    for number in nums:
        memory[number] = number+1

    for key, value in memory.items():
        print(key, value)

    count = 0
    tempCount = 1

    for key, value in memory.items():
        tempCount = 1
        currentVal = key
        while(currentVal in memory.keys()):
            if memory[currentVal] in memory.keys():
                tempCount = tempCount + 1
                currentVal = memory[currentVal]

            currentVal = memory[currentVal]
            print("in while loop")
        if tempCount > count:
            count = tempCount
    
    return count
    

# This is the brute-force solution. i believe the sort method occurs in nlogn time
def longestConsecutiveBF(nums: List[int]) -> int:
   
    sortedList = sorted(nums)
    maxSeq = 0
    tempSeq = 1
   
    for index in range(len(sortedList)-1):
        if sortedList[index+1] == sortedList[index] + 1:
            tempSeq = tempSeq + 1
        else:
            tempSeq = 1
        if tempSeq > maxSeq:
            maxSeq = tempSeq

    return maxSeq


print(longestConsecutiveOptimal(input))
#print(longestConsecutiveBF(input))
#print(longestConsecutiveBF(input2))
