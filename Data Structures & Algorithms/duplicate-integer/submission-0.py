from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict = Counter(nums)
        status = False
        for value in dict.values():
            if value > 1:
                status = True
        return status
            
        