class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap1 = [-n for n in nums if n >= 0]
        maxHeap2 = [abs(n) for n in nums if n < 0]
        heapq.heapify(maxHeap1)
        heapq.heapify(maxHeap2)
        print(maxHeap1)
        print(maxHeap2)
        
        
        while k > 1 and maxHeap1:
            heapq.heappop(maxHeap1)
            k -= 1
        
        if k == 1 and maxHeap1:
            return abs(maxHeap1[0])
        
        while k > 1 and maxHeap2:
            heapq.heappop(maxHeap2)
            k -= 1
            
        if k == 1 and maxHeap2: 
            return -(maxHeap2[0])
            
        