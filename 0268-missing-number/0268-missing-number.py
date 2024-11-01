class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num = len(nums)
        total = 0
        
        for i in range(num+1):
            total += i
        
        for i in nums:
            total -= i
        
        return total