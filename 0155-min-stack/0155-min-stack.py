class MinStack:

    def __init__(self):
        self.minstack = []
        self.minVals = []

    def push(self, val: int) -> None:
        self.minstack.append(val)
        val = min(val, self.minVals[-1] if self.minVals else val)
        self.minVals.append(val)
        

    def pop(self) -> None:
        self.minVals.pop()
        return self.minstack.pop()
        

    def top(self) -> int:
        return self.minstack[-1]

    def getMin(self) -> int:
        return self.minVals[-1]

        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()