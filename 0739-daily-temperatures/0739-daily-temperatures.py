class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        
        for i,t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                temp, index = stack.pop()
                res[index] = (i - index)
            stack.append([i,t])
        
        return res