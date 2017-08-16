# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        q = collections.deque([root])
        level = 0
        while q:
            level += 1
            for i in xrange(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                if not node.left and not node.right:
                    return level
        return -1



class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return self.getMin(root)

    def getMin(self, root):
        if not root:
            return sys.maxint
        if not root.left and not root.right:
            return 1
        return min(self.getMin(root.left), self.getMin(root.right)) + 1
