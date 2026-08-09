# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def dfs(node):
            if node is None:
                return 0
            
            leftDepth  = dfs(node.left)
            rightDepth = dfs(node.right)

            return 1 + max(leftDepth, rightDepth)
        ans = dfs(root)
        return ans
