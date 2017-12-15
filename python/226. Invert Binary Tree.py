# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        self.helper(root)
        return root

    def helper(self, root):
        if not root:
            return
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)



class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root
        self.invertTree(root.left)
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        return root








# BFS
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        q = collections.deque([root])
        while q:
            cur = q.popleft()
            cur.left, cur.right = cur.right, cur.left
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
        return root

# DFS
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root:
            stack = [root]
            while q:
                cur = stack.pop()
                cur.left, cur.right = cur.right, cur.left
                if cur.left:
                    stack.append(cur.left)
                if cur.right:
                    stack.append(cur.right)
        return root
