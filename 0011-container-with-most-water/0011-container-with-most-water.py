class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxWater = 0
        l,r = 0, len(height) - 1
        
        while l < r:
            maxWater = max(maxWater, min(height[l], height[r]) * (r-l))
            if height[r] < height[l]:
                r -= 1
            else:
                l += 1
        return maxWater
            
            