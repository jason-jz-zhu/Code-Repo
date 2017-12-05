# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []

        res = []
        q = collections.deque([(root, 0)])
        hashmap = collections.defaultdict(list)

        while q:
            node, level = q.popleft()
            hashmap[level].append(node.val)
            if node.left:
                q.append((node.left, level - 1))
            if node.right:
                q.append((node.right, level + 1))

        for k, v in sorted(hashmap.items(), key = lambda (k, v): (k, v)):
            res.append(v)

        return res
