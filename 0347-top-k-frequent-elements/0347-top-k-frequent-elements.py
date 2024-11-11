class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        res = []
        maxHeap = []
        
        for v,c in count.items():
            maxHeap.append([-c,v])
        
        heapq.heapify(maxHeap)
        
        while k > 0:
            res.append(heapq.heappop(maxHeap)[1])
            k -= 1
        
        return res