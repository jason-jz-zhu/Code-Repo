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
        if root is None:
            return []
        res = []
        self.dfs(root, '', res)
        return res

    def dfs(self, node, path, res):
        if not node.right and not node.left:
            res.append(path + str(node.val))
        if node.right:
            self.dfs(node.right, path + str(node.val) + '->', res)
        if node.left:
            self.dfs(node.left, path + str(node.val) + '->', res)
