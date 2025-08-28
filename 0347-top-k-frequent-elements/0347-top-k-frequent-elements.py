class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        countGrouped = [[] for i in range(len(nums)+1)]
        res = []

        for key, value in count.items():
            countGrouped[value].append(key)

        for i in range(len(nums),-1,-1):
            for n in countGrouped[i]:
                res.append(n)
                if len(res) == k:
                    return res
        
        return []