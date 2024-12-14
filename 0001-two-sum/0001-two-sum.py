class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevNums = {}
        
        for i, num in enumerate(nums):
            if target - num in prevNums:
                return [i, prevNums[target - num]]
            prevNums[num] = i
        
        return []
        