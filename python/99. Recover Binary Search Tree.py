# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# O(n) space
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        def helper(root):
            if root:
                helper(root.left)
                self.nodes.append(root)
                self.vals.append(root.val)
                helper(root.right)

        self.nodes = []
        self.vals = []
        helper(root)
        self.vals.sort()
        for i in xrange(len(self.nodes)):
            self.nodes[i].val = self.vals[i]


# O(1) space
# Morris Traversal
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root is None:
            return

        broken = [None, None]
        cur = root
        pre = None

        while cur:
            if cur.left is None:
                # deal with val
                self.detectBroken(broken, pre, cur)
                pre = cur
                cur = cur.right
            else:
                node = cur.left
                while node.right and node.right != cur:
                    node = node.right

                if node.right is None:
                    node.right = cur
                    cur = cur.left
                else:
                    node.right = None
                    # deal with val
                    self.detectBroken(broken, pre, cur)
                    pre = cur
                    cur = cur.right
        broken[0].val, broken[1].val = broken[1].val, broken[0].val


    def detectBroken(self, broken, pre, cur):
        if pre and pre.val > cur.val:
            if broken[0] is None:
                broken[0] = pre
            broken[1] = cur
