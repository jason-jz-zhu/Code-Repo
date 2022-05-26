# bfs
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return None
        ans = []
        q = deque([root])
        
        while q:
            ans.append([node.val for node in q])
            q = [child for node in q for child in node.children if child]
        return ans

# dfs
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        def dfs(node, level):
            if not root:
                return
            if level == len(ans):
                ans.append([])
            ans[level].append(node.val)
            for child in node.children:
                dfs(child, level + 1)
            
        ans = []
        dfs(root, 0)
        return ans
