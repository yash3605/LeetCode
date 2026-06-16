class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            else:
                subStr = ""
                while stack[-1] != "[":
                    subStr = stack.pop() + subStr
                stack.pop()

                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                stack.append(int(k) * subStr)
        return "".join(stack)
        

solution = Solution()
print(solution.decodeString("3[a]2[bc]"))
print(solution.decodeString("3[a2[c]]"))
print(solution.decodeString("2[abc]3[cd]ef"))
print(solution.decodeString("2[a3[b]]c"))
print(solution.decodeString("axb3[z]4[c]"))
print(solution.decodeString("ab2[c]3[d]1[x]"))
