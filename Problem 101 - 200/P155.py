'''
The key point is to maintain the minimum value
with pop and push operations.
It needs extra space for constant time complexity functions.

'''
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        # value is tuple (x, m), m is the minimum
        # from bottom to value x.
        self.stack = []

    def push(self, x: int) -> None:
        m = self.getMin()
        self.stack.append((x, min(x, m)))

    def pop(self) -> None:
        self.stack.pop()        

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        if not self.stack:
            return float('inf')
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()