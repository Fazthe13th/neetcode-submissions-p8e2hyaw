from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped = defaultdict(list)
        for s in strs:
            sorteds = ''.join(sorted(s))
            grouped[sorteds].append(s)
        return list(grouped.values())
        