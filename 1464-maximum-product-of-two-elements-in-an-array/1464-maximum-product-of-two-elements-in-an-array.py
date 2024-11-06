class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxHeap = [-n for n in nums]
        heapq.heapify(maxHeap)
        first,second = heapq.heappop(maxHeap) + 1, heapq.heappop(maxHeap) + 1
        return first * second