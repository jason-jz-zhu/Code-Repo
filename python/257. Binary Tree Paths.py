# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# dfs and stack
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root is None:
            return []
        res, stack = [], [(root, '')]
        while stack:
            node, path = stack.pop()
            if not node.right and not node.left:
                res.append(path + str(node.val))
            if node.right:
                stack.append((node.right, path + str(node.val) + '->'))
            if node.left:
                stack.append((node.left, path + str(node.val) + '->'))
        return res

# bfs and queue
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root is None:
            return []
        res, queue = [], collections.deque([(root, "")])
        while queue:
            node, path = queue.popleft()
            if not node.left and not node.right:
                res.append(path + str(node.val))
            if node.left:
                queue.append((node.left, path + str(node.val) + '->'))
            if node.right:
                queue.append((node.right, path + str(node.val) + '->'))
        return res

# dfs and recursively
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        res = []
        self.helper(root, '', res)
        return res

    def helper(self, root, path, res):
        if not root:
            return
        if not root.left and not root.right:
            res.append(path + str(root.val))
        self.helper(root.left, path + str(root.val) + '->', res)
        self.helper(root.right, path + str(root.val) + '->', res)
