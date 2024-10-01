class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}
        res = []
        
        for i,n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [i, prevMap[diff]]
            prevMap[n] = i
            