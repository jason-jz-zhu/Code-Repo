# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# dfs recursive
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        res = []
        self.helper(root, res)
        return res

    def helper(self, node, res):
        if not node:
            return
        res.append(node.val)
        self.helper(node.left, res)
        self.helper(node.right, res)


class Solution:
    # 定义：输入一棵二叉树的根节点，返回这棵树的前序遍历结果
    def preorderTraversal(self, root):
        res = []
        if root == None:
            return res
        # 前序遍历的结果，root.val 在第一个
        res.append(root.val)
        # 利用函数定义，后面接着左子树的前序遍历结果
        res.extend(self.preorderTraversal(root.left))
        # 利用函数定义，最后接着右子树的前序遍历结果
        res.extend(self.preorderTraversal(root.right)) 

        return res




# dfs interative
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res