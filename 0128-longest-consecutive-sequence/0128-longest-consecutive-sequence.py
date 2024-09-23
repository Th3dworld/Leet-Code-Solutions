class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet = set(nums)
        longest = 0
        
        for n in hashSet:
            number = n
            if n-1 not in hashSet:
                length = 1
                while number + 1 in hashSet:
                    length += 1
                    number += 1
                longest = max(length, longest)
        return longest
                
        
        