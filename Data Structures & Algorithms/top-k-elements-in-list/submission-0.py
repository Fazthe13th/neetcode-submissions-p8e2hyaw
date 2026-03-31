from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # counter = Counter(nums)
        # return [value[0] for i , value in enumerate(counter.most_common(k))]
        count = defaultdict(list)
        freq = [[] for i in range(len(nums) + 1)]
        for num in nums:
            count[num] = count.get(num,0) + 1
        for num , c in count.items():
            freq[c].append(num)
        result = []
        for i in range(len(freq) - 1,0, -1):
            for num in freq[i]:
                result.append(num)
                if len(result) == k:
                    return result



        