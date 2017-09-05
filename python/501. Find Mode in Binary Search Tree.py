# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        def inorder(root):
            if not root:
                return
            inorder(root.left)

            if root.val != self.pre:
                self.cnt = 1
                self.pre = root.val
            else:
                self.cnt += 1

            if self.cnt > self.max_cnt:
                self.max_cnt = self.cnt
                del self.res[:]
                self.res.append(root.val)
            elif self.cnt == self.max_cnt:
                self.res.append(root.val)

            inorder(root.right)

        self.res = []
        self.pre = sys.maxint
        self.cnt = 1
        self.max_cnt = 0
        inorder(root)
        return self.res
