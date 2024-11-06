import heapq

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        lenq = len(nums)
        res = [0] * k
        heap = []
        
        for i in range(len(nums)):
            heap.append([nums[i], i])
            
        heapq.heapify(heap)
        
        while lenq > k:
            heapq.heappop(heap)
            lenq -= 1
        
        heap1 = []
        
        while heap:
            currVal = heapq.heappop(heap)
            heap1.append([currVal[1], currVal[0]])
        
        heapq.heapify(heap1)
        
        res = []
        
        while heap1:
            res.append(heapq.heappop(heap1)[1])
        
        return res
        
        
        
        