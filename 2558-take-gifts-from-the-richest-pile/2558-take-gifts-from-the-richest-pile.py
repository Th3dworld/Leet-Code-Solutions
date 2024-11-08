class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        maxHeap = [-g for g in gifts]
        heapq.heapify(maxHeap)
        total = 0
        
        while k > 0:
            val = abs(heapq.heappop(maxHeap))
            heapq.heappush(maxHeap, -floor(sqrt(val))) 
            k -= 1
        
        while maxHeap:
            total += abs(heapq.heappop(maxHeap))
        
        return total