class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}
        
        for i,v in enumerate(nums):
            if target - v in prevMap:
                return [i, prevMap[target - v]]
            prevMap[v] = i
        
        return prevMap