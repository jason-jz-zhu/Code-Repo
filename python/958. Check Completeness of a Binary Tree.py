# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        q = collections.deque([root])
        missing = False
        while q:
            size = len(q)
            while size > 0:
                size -= 1
                node = q.popleft()
                if node:
                    if missing:
                        return False
                    q.append(node.left)
                    q.append(node.right)
                else:
                    missing = True
        return True
