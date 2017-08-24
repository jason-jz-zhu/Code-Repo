# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = []
        rank = 0
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                rank += 1
                if rank == k:
                    return root.val
                root = root.right
        return float('-inf')

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        def helper(root):
            if root:
                helper(root.left)
                self.rank += 1
                if self.rank == k:
                    self.res = root.val
                    return
                helper(root.right)
        self. res = None
        self.rank = 0
        helper(root)
        return self.res

# 如果BST节点TreeNode的属性可以扩展，则再添加一个属性leftCnt，记录左子树的节点个数
#记当前节点为node
#当node不为空时循环：
#若k == node.leftCnt + 1：则返回node
#否则，若k > node.leftCnt：则令k -= node.leftCnt + 1，令node = node.right
#否则，node = node.left
