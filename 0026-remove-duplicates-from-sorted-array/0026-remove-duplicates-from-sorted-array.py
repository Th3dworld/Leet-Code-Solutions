class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique = len(nums)
        if unique == 1: return 1
        
        s,f = 0,1
        while f < len(nums):
            if nums[s] == nums[f] and s != f:
                nums[f] = '_'
                unique -= 1
            else:
                s += 1
                nums[s] = nums[f]
            f += 1
        return unique