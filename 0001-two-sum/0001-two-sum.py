class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        valueToIndex = {}
        
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in valueToIndex:
                return [i, valueToIndex[diff]]
            valueToIndex[nums[i]] = i
            