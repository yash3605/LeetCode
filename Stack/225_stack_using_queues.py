"""
LeetCode #225: Implement Stack using Queues

Implement a last-in-first-out (LIFO) stack using only two queues. Implement the MyStack class: MyStack() initializes the stack object, void push(int x) pushes element x onto the stack, int pop() removes the element on top of the stack, int top() returns the element on top of the stack, boolean empty() returns true if the stack is empty.

Constraints:
1 <= x <= 9, At most 100 calls will be made to push, pop, top, and empty.
"""
from collections import deque
class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
        
    def push(self, x: int) -> None:
        self.q2.append(x)
        while self.q1:
            self.q2.append(self.q1.popleft())
        
        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:
        return self.q1.popleft()

    def top(self) -> int:
        return self.q1[0]
        
    def empty(self) -> bool:
        return len(self.q1) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
