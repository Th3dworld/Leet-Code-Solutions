class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for i in range(len(nums) + 1)]
        count = Counter(nums)
        
        for key,v in count.items():
            bucket[v].append(key)
        
        res = []
        print(bucket)
        
        for i in range(len(nums),0,-1):
            for j in bucket[i]:
                res.append(j)
                
                if len(res) == k:
                    return res
        
        return []