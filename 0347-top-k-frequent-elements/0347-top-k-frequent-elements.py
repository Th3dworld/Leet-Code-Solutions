class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for _ in range(len(nums) + 1)]
        count = Counter(nums)

        for v,c in count.items():
            bucket[c].append(v)
        
        res = []

        for i in range(len(nums),-1,-1):
            for v in bucket[i]:
                res.append(v)
                if len(res) == k:
                    return res
