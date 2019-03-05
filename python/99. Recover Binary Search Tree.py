# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# O(n) space
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        vals = []
        nodes = []
        self.dfs(root, vals, nodes)
        vals.sort()
        for i, node in enumerate(nodes):
            node.val = vals[i]

    def dfs(self, node, vals, nodes):
        if not node:
            return
        self.dfs(node.left, vals, nodes)
        vals.append(node.val)
        nodes.append(node)
        self.dfs(node.right, vals, nodes)


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
