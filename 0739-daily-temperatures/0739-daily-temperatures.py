class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #[day,temp]
        #answer
        stack = []
        answer = [0] * len(temperatures)

        for i,v in enumerate(temperatures):
            while stack and stack[-1][1] < v:
                index, value = stack.pop()
                print(index)
                answer[index] = i - index
            stack.append([i,v])
        
        return answer
                