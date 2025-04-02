class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        res = []
        bucket = [[] for i in range(len(nums) + 1)]

        for val, count in count.items():
            bucket[count].append(val)
        
        for i in range(len(bucket)-1,-1,-1):
            for val in bucket[i]:
                res.append(val)
                if len(res) == k:
                    return res
        
        return []