# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        left_height = right_height = 0
        left_node, right_node = root, root
        while left_node:
            left_height += 1
            left_node = left_node.left

        while right_node:
            right_height += 1
            right_node = right_node.right

        if left_height == right_height:
            return 2 ** left_height - 1

        return self.countNodes(root.left) + self.countNodes(root.right) + 1

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = 0

        while root:
            llh = self.leftDepth(root.left)
            lrh = self.rightDepth(root.left)
            rrh = self.rightDepth(root.right)

            if llh == rrh:
                res += (1 << llh+1) - 1
                break
            elif llh > lrh:
                res += 1 << rrh
                root = root.left
            else:
                res += 1 << llh
                root = root.right
        return res

    def leftDepth(self, root):
        return self.leftDepth(root.left) + 1 if root else 0

    def rightDepth(self, root):
        return self.rightDepth(root.right) + 1 if root else 0
