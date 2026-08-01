"""
LeetCode #150: Evaluate Reverse Polish Notation

Evaluate the value of an expression in Reverse Polish Notation. Valid operators are +, -, *, /. Each operand may be an integer or another expression. Note that division between two integers should truncate toward zero. There will not be any division by zero.

Constraints:
1 <= tokens.length <= 10^4, tokens[i] is either an operator: "+", "-", "*", "/" or an integer in the range [-200, 200].
"""
class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b) / a))
            else:
                stack.append(int(c))
        return stack[0]


solution = Solution()
print(solution.evalRPN(["2", "1", "+", "3", "*"]))
print(solution.evalRPN(["4", "13", "5", "/", "+"]))
print(solution.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
print(solution.evalRPN(["1","2","+","3","*","4","-"]))
