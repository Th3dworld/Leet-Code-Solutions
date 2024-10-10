class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        Map = {}
        for i,v in enumerate(nums):
            diff = target - v
            if diff in Map:
                return [i, Map[diff]]
            Map[v] = i