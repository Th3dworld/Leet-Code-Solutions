class Solution:
    def trap(self, height: List[int]) -> int:
        left,right = 0, len(height) - 1
        maxLeft, maxRight = 0, 0
        res = 0

        while left < right:
            if height[left] < height[right]:
                maxLeft = max(height[left], maxLeft)
                res += maxLeft - height[left]
                left += 1
            else:
                maxRight = max(height[right], maxRight)
                res += maxRight - height[right]
                right -= 1
        
        return res