class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for i in range(len(nums) + 1)]
        count = Counter(nums)
        res = []

        for v,f in count.items():
            bucket[f].append(v)
        
        for i in range(len(nums),-1,-1):
            for v in bucket[i]:
                res.append(v)
                if len(res) == k:
                    return res
        