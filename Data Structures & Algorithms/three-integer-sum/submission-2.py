class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i, a in enumerate(nums):
            # BREAK if the first number is greater than 0
            # because we are looking for triplets that sum to 0
            if a > 0: 
                break
            # Skip duplicates for the first number
            # to avoid duplicate triplets in the result
            if i > 0 and a == nums[i-1]:
                continue
            # Two pointers for the second and third numbers
            # left pointer starts just after the first number
            left = i + 1
            right = len(nums) - 1
            while left < right:
                sum = nums[left] + nums[right] + a
                if sum > 0:
                    right -= 1
                elif sum < 0:
                    left += 1                    
                else:
                    res.append([a, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        return res