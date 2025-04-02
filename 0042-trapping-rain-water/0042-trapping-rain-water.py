class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft, maxRight = height[0], height[len(height) - 1]
        l,r = 0, len(height) - 1
        total = 0

        while l < r:
            if maxRight > maxLeft:
                l += 1
                maxLeft = max(maxLeft, height[l])
                total += maxLeft - height[l]
            else:
                r -= 1
                maxRight = max(maxRight, height[r])
                total += maxRight - height[r]
            
        return total
