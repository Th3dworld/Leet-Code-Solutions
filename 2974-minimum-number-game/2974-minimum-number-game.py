class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        heapq.heapify(nums)
        res = []
        
        while nums:
            Alice, Bob = heapq.heappop(nums), heapq.heappop(nums)
            res.append(Bob)
            res.append(Alice)     
        
        return res