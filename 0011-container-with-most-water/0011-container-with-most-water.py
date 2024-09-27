class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r,res = 0, len(height) - 1, 0
        
        while l < r:
            area = 0
            dist = r-l
            if height[l] < height[r]:
                area = height[l] * dist
                l += 1
            elif height[r] < height[l]:
                area = height[r] * dist
                r -= 1
            else:
                area = height[r] * dist
                r -= 1
                l += 1
            res = max(res,area)
        return res