# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# binary serach o(h) o (1)
class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        if not root or not p:
            return None
        res = None
        while root:
            res = root if p.val < root.val else res
            root = root.left if p.val < root.val else root.right
        return res

# dfs interative inorder o(n) o (n)
class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        if not root or not p:
            return None
        flag = False
        stack = []
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                if flag:
                    return root
                if root.val == p.val:
                    flag = True
                root = root.right
        return None


class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        res = []
        self.inorder(root, p, [False], res)
        return res[0] if len(res) != 0 else None

    def inorder(self, root, p, flag, res):
        if not root:
            return

        self.inorder(root.left, p, flag, res)
        if flag[0]:
            res.append(root)
        if p.val == root.val:
            flag[0] = True
        self.inorder(root.right, p, flag, res)
