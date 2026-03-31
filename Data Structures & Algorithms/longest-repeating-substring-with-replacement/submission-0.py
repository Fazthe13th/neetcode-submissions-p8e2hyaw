

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l , r = 0 , 0
        count_dict = {}
        max_langth = 0
        current_max_count = 0
        for r in range(len(s)):
            count_dict[s[r]] = count_dict.get(s[r], 0) + 1
            current_max_count = max(current_max_count, count_dict[s[r]])
            while len(s[l:r+1]) - current_max_count > k:
                count_dict[s[l]] -= 1
                l += 1
            max_langth = max(max_langth, len(s[l:r+1]))
        return max_langth



        