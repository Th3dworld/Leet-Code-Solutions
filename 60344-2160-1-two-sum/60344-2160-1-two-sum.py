class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Map = {}
        
        for i,v in enumerate(nums):
            if target - v in Map:
                return [Map[target-v], i]
            Map[v] = i