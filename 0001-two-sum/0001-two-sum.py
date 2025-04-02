class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ValueToIndex = {}
        
        for i,v in enumerate(nums):
            if target - v in ValueToIndex:
                return [ValueToIndex[target - v], i]
            ValueToIndex[v] = i
        
        return []