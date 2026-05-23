class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        self.minStack.append(min(val, self.minStack[-1] if self.minStack else val))
        

    def pop(self) -> None:
        self.minStack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]

minstack = MinStack()
minstack.push(1)
minstack.push(2)
minstack.push(0)
print(minstack.getMin())
minstack.pop()
print(minstack.top())
print(minstack.getMin())
