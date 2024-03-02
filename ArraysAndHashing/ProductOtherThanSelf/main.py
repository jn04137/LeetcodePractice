from typing import List

"""
Have to figure out how the elements other than the selected index are multiplied together
to get the product for the selected index

Do I need buckets? Do I need to add a map to hold onto values?

I think I gave myself a hint. Maybe a map to store the value and position of each element
in the array?

Have prefix and postfix arrays with calculated values ready to be used later on
"""

class Product:
    # optimized solution

    def optimized(nums: List[int]) -> List[int]:
        res_list = [1 for i in range(len(nums))]

        # This is setting the prefix on the result list
        for i in range(len(nums)):
            if i == 0:
                res_list[i] = 1
            else:
                res_list[i] = res_list[i - 1] * nums[i - 1]

        print(str(res_list))

        # This is setting the post fix on the result list
        # Need to store postfix value with previously counted postfix values
        postfix = 1
        for i in reversed(range(len(nums))):
            if i == len(nums) - 1:
                continue;
            else:
                postfix = postfix * nums[i+1]
                res_list[i] = res_list[i] * postfix


        return res_list

    # Somewhat optimized solution
    def productExceptSelf(nums: List[int]) -> List[int]:
        print("This is the list of nums: " + str(nums))
        prefix = nums.copy()
        postfix = nums.copy()
        res_list = [1 for i in range(len(nums))]

        for i in range(len(prefix)):
            if i != 0:
                prefix[i] = prefix[i] * prefix[i - 1]

        for i in reversed(range(len(postfix))):
            print(i)
            if i != len(postfix) - 1:
                postfix[i] = postfix[i] * postfix[i + 1]

        for i in range(len(nums)):
            if i == 0:
                res_list[i] = postfix[i+1]
            elif i == len(nums) - 1:
                res_list[i] = prefix[i-1]
            else:
                res_list[i] = prefix[i-1] * postfix[i+1]

        return res_list
