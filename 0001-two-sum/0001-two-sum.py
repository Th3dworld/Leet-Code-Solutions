class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        valueToIndex = {}

        for index,value in enumerate(nums):
            if target - value in valueToIndex:
                return [index, valueToIndex[target - value]]
            valueToIndex[value] = index
        
        return []