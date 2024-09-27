class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r,res = 0, len(height) - 1, 0
        
        while l < r:
            res = max(res, min(height[l], height[r]) * (r-l))
            if height[l] < height[r]:
                l += 1
            elif height[r] < height[l]:
                r -= 1
            else:
                l += 1
                r -= 1
        return res