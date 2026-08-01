"""
LeetCode #155: Min Stack

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time. Implement the MinStack class: MinStack() initializes the stack object, void push(int val) pushes the element val onto the stack, void pop() removes the element on the top of the stack, int top() gets the top element of the stack, int getMin() retrieves the minimum element in the stack.

Constraints:
-2^31 <= val <= 2^31 - 1, pop, top and getMin operations will always be called on non-empty stacks.
"""
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
