class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        frequency = [[] for i in range(len(nums) + 1)]
        
        for n in nums:
            count[n] = count.get(n,0) + 1
        
        
        for n, c in count.items():
            frequency[c].append(n)
        
        res = []
        
        for i in range(len(frequency) - 1,0,-1):
            for n in frequency[i]:
                res.append(n)
                if len(res) == k:
                    return res
