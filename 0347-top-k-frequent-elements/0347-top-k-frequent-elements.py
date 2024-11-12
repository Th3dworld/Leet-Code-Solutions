class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for i in range(len(nums) + 1)]
        count = Counter(nums)
        
        for val, cnt in count.items():
            bucket[cnt].append(val)
        
        res = []
        
        for i in range(len(nums),0,-1):
            for j in bucket[i]:
                res.append(j)
                if len(res) == k:
                    return res                    
        
