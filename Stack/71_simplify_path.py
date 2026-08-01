"""
LeetCode #71: Simplify Path

Given a string path, which is an absolute path (starting with a slash '/') to a file or directory in a Unix-style file system, convert it to the simplified canonical path. A canonical path must always begin with a slash '/', any two directory names must be separated by a single slash '/', and the path must not end with a trailing '/'.

Constraints:
1 <= path.length <= 3000, path consists of English letters, digits, period '.', slash '/' or '_'.
"""
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
