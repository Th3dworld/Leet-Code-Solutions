class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] #(start, height)
        largest = 0

        for i,h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                largest = max(largest, height * (i - index))
                start = index
            stack.append((start, h))
        
        for s,h in stack:
            largest = max(largest, h * (len(heights) - s))

        return largest