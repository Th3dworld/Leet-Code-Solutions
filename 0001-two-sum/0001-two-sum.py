class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numToIndex = {}

        for i,v in enumerate(nums):
            if target - v in numToIndex:
                return [i , numToIndex[target - v]]
            numToIndex[v] = i
        
        return []