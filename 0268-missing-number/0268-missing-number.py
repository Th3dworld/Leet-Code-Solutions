class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        set1 = set(nums)
        set2 = set(range(max(nums)+1))
        set3 = set2 - set1

        if(set3 == set()):
            return max(nums) + 1
        else:  
            return list(set3)[0]