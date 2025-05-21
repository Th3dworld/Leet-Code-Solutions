class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        valueToIndex = {}

        for i,v in enumerate(nums):
            if target - v in valueToIndex:
                return [valueToIndex[target-v], i]
            valueToIndex[v] = i
        
        return []
