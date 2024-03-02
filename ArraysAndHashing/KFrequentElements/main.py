from typing import List

class Solution:

    def topKFrequent(nums: List[int], k: int) -> List[int]:

        # Just use a hashap to help count the occurences
        # Will store the key in a list where index of result equals the occurence
        # Traverse through the list in reverse to find the k-most occuring values

        occ_map = {}
        bucket = [[] for i in range(len(nums) + 1)]
        result = []

        count = 0

        if len(nums) == 1:
            return nums

        for num in nums:
            if num in occ_map:
                occ_map[num] = occ_map[num] + 1
            else:
                occ_map[num] = 1

        for key, value in occ_map.items():
            bucket[value].append(key)

        for i in reversed(range(len(bucket))):
            if bucket[i] == None:
                continue
            if len(result) != k:
                result = result + bucket[i]

        return result
