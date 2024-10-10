class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        Map = Counter(nums)
        bucket = [[] for i in range(len(nums) + 1)]
        
        for key, v in Map.items():
            bucket[v].append(key)
            
        res = []
        
        for i in range(len(nums),-1,-1):
                res += bucket[i]
                if len(res) == k:
                    return res
        