class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for i in range(len(nums)+ 1)]
        res = []
        count = Counter(nums)
        
        for v,c in count.items():
            bucket[c].append(v)
        
        for i in range(len(nums), 0,-1):
            for v in bucket[i]:
                res.append(v)
                if len(res) == k:
                    return res
                
        