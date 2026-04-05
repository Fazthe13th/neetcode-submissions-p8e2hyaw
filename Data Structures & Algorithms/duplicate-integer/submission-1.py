class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        c = 0
        s = set()
        for i in range(len(nums)):
            if nums[i] in s:
                return True
            else:
                s.add(nums[i])
        return False