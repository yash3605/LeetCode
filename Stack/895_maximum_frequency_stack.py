"""
LeetCode #895: Maximum Frequency Stack

Design a stack-like data structure to push elements to the stack and pop the most frequent element from the stack. Implement the FreqStack class: FreqStack() initializes the empty frequency stack, void push(int val) pushes an integer val onto the top of the stack, int pop() removes and returns the most frequent element in the stack. If there is a tie for the most frequent element, the element closest to the top is removed.

Constraints:
0 <= val <= 10^9, At most 2 * 10^4 calls will be made to push and pop.
"""
class FreqStack:

    def __init__(self):
        self.stacks = [[]]
        self.cnt = {}
        
    def push(self, val: int) -> None:
        valCnt = 1 + self.cnt.get(val, 0)
        self.cnt[val] = valCnt

        if valCnt == len(self.stacks):
            self.stacks.append([])
        self.stacks[valCnt].append(val)

    def pop(self) -> int:
        res = self.stacks[-1].pop()
        self.cnt[res] -= 1

        if not self.stacks[-1]:
            self.stacks.pop()

        return res

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()

freqStack = FreqStack()
print(freqStack.push(5))
print(freqStack.push(7))
print(freqStack.push(5))
print(freqStack.push(7))
print(freqStack.push(4))
print(freqStack.push(5))
print(freqStack.pop())
print(freqStack.pop())
print(freqStack.pop())
print(freqStack.pop())
