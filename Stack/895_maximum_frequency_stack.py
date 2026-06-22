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
