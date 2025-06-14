class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        valueToIndex = {}
        
        for index,value in enumerate(nums):
            diff = target - value

            if diff in valueToIndex:
                return [valueToIndex[diff], index]

            valueToIndex[value] = index
        
        return []

        