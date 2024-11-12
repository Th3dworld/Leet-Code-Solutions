class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet = set(nums)
        longest = 0
        
        for i in range(len(nums)):
            if nums[i] - 1 not in hashSet:
                length = 0
                
                while nums[i] + length in hashSet:
                    length += 1
                
                longest = max(length, longest)
        
        return longest