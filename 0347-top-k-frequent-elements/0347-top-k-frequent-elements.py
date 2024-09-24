class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        
        for n in nums:
            count[n] = count.get(n,0) + 1

        for n,f in count.items():
            freq[f].append(n)
        
        res = []
        
        for i in range(len(nums),-1,-1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res