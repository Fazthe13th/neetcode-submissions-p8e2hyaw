class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = dict()
        for i,s in enumerate(strs):
            key = "".join(sorted(s))
            if key not in seen:
                seen[key] = []
            seen[key].append(i)
        result = []
        for key,value in seen.items():
            sublist = [strs[i] for i in value]
            result.append(sublist)
        return result