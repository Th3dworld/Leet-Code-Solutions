class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numToIndex = {}
        
        for i,n in enumerate(nums):
            diff = target - n
            if diff in numToIndex:
                return [i, numToIndex[diff]]
            numToIndex[n] = i