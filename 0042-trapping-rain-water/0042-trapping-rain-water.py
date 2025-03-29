class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft, maxRight = height[0], height[len(height)-1]
        l,r = 0, len(height)-1
        total = 0

        while l < r:
            if height[l] < height[r]:
                maxLeft = max(maxLeft, height[l])
                total += maxLeft - height[l]
                l += 1
            else:
                maxRight = max(maxRight, height[r])
                total += maxRight - height[r]
                r -= 1
        
        return total
            