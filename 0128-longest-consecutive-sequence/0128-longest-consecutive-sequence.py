class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet = set(nums)
        maxLength = 0
        
        for i in nums:
            if i-1 not in hashSet:
                length = 0
                while i + length in hashSet:
                    length += 1
                maxLength = max(maxLength, length)
        
        return maxLength
                    