class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        final_longest = 0
        for num in set_nums:
            longest = 0
            if num - 1 not in set_nums:
                longest = 1
                start = num
                while num + longest in set_nums:
                    longest += 1
            final_longest = max(longest,final_longest)
        return final_longest

