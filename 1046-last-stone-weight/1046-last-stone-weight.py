class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-s for s in stones]
        heapq.heapify(maxHeap)
        
        while len(maxHeap) > 1:
            first, second = abs(heapq.heappop(maxHeap)), abs(heapq.heappop(maxHeap))
            
            if first != second:
                heapq.heappush(maxHeap, -(first - second))
        
        if maxHeap:
            return abs(heapq.heappop(maxHeap))
        else:
            return 0