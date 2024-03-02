# Two sum kind of looks like a two pointer problem
# Maybe we can do it with one pointer?
def two_sum(nums: list[int], target: int) -> list[int]:
    hashmap = {}

    for index in range(len(nums)):
        if target - nums[index] in hashmap:
            return [hashmap[target-nums[index]], index]
        hashmap[nums[index]] = index
