# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        res = 0
        q = collections.deque([(root, False)])
        while q:
            curr, is_left = q.popleft()
            if is_left and not curr.left and not curr.right:
                res += curr.val
            if curr.left:
                q.append((curr.left, True))
            if curr.right:
                q.append((curr.right, False))
        return res


class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        self.res = 0
        self.helper(root, False)
        return self.res

    def helper(self, root, is_left):
        if not root:
            return
        if is_left and not root.left and not root.right:
            self.res += root.val
        self.helper(root.left, True)
        self.helper(root.right, False)
