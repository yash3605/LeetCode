from collections import deque

# DFS (Depth-first Search, Pre-Order)
def dfs(node):
    if node is None:
        return base_value # e.g. 0, False, float('-inf')
    
    left = dfs(node.left)
    right = dfs(node.right)

    return combine(node.val, left, right) # for postorder - (left, right, node.val) & for inorder - (left, node.val, right)

# BFS (Breadth-first Search, Level Order)
def bfs(root):
    if not root:
        return []
    
    queue = deque([root])
    result = []

    while queue:
        level_size = len(queue)
        level = []

        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)
    return result
