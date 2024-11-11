class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        nums = []
        res = []
        
        for v,c in count.items():
            nums.append([-c, v])
        
        heapq.heapify(nums)
        
        while k > 0:
            res.append(heapq.heappop(nums)[1])
            k -= 1
        
        return res
        

            