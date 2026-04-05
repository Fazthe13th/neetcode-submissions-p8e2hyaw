
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for num in nums:
            if num in counter:
                counter[num] = counter[num] + 1
            else:
                counter[num] = 1
        heap = []
        for key, val in counter.items():
            heapq.heappush(heap, (val,key))
            if len(heap) > k:
                heapq.heappop(heap)
        return [item[1] for item in heap]