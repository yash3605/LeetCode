class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        cur = ""

        for c in path + "/":
            if c == "/":
                if cur == "..":
                    if stack:
                        stack.pop()
                elif cur != "" and cur != ".":
                    stack.append(cur)
                cur = ""
            else:
                cur += c

        return "/" + "/".join(stack)


        

solution = Solution()
print(solution.simplifyPath("/neetcode/practice//...///../courses"))
print(solution.simplifyPath("/..//"))
print(solution.simplifyPath("/..//_home/a/b/..///"))
print(solution.simplifyPath("/home/"))
print(solution.simplifyPath("/home//foo/"))
print(solution.simplifyPath("/home/user/Documents/../Pictures"))
print(solution.simplifyPath("/../"))
print(solution.simplifyPath("/.../a/../b/c/../d/./"))
