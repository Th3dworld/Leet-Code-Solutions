class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        Set = set(nums)
        Max = 0
        
        for i in Set:
            n = i
            count = 1
            if n-1 in Set:
                continue
            else:
                while n + 1 in Set:
                    count += 1
                    n += 1
                Max = max(count, Max)
        return Max