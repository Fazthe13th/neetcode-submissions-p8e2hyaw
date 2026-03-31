import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # index = 0
        # result = []
        # while index < len(nums):
        #     nums_temp = nums.copy()
        #     nums_temp.pop(index)
        #     result.append(math.prod(nums_temp))
        #     index += 1
        # return result
        prefix = 1
        postfix = 1
        output = [1] * len(nums)
        for i in range(len(nums)):
            output[i] = prefix
            prefix = prefix * nums[i]
        for i in range(len(nums) - 1, -1 , -1):
            output[i] = output[i] * postfix
            postfix = postfix * nums[i]
        return output

        