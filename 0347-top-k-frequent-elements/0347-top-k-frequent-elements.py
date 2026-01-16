class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countr = Counter(nums)
        sortr = [[] for i in range(len(nums) + 1)]
        res = []

        for val, count in countr.items():
            sortr[count].append(val)

        for i in range(len(nums),0,-1):
            for n in sortr[i]:
                res.append(n)
                if len(res) == k:
                    return res