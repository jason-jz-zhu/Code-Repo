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
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
            return root



class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root:
            q = collections.deque([root])
            while q:
                cur = q.popleft()
                cur.left, cur.right = cur.right, cur.left
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
        return root

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root:
            q = [root]
            while q:
                cur = q.pop()
                cur.left, cur.right = cur.right, cur.left
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
        return root
