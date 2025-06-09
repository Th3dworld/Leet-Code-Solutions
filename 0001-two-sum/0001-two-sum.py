class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        valueToIndex = {}

        for val, ind in enumerate(nums):
            if target - val in valueToIndex:
                return [valueToIndex[target - val], ind]
            valueToIndex[val] = ind
        
        return []