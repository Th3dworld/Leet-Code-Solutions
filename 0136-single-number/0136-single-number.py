class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = Counter(nums)
        
        for v,c in count.items():
            if c == 1:
                return v