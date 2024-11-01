class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        self.maxHeap = [-s for s in stones]
        heapq.heapify(self.maxHeap)
        
        while len(self.maxHeap) > 1:
            one,two = heapq.heappop(self.maxHeap),heapq.heappop(self.maxHeap)
            if abs(one) - abs(two) != 0:
                heapq.heappush(self.maxHeap, -(abs(one) - abs(two)))
        if len(self.maxHeap) > 0:
            return abs(self.maxHeap[0])
        else:
            return 0