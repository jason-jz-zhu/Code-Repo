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
        res = []
        if root is None:
            return res
        q = collections.deque([(root, 0)])
        hashmap = {}
        while q:
            head, level = q.popleft()
            if level in hashmap:
                hashmap[level].append(head.val)
            else:
                hashmap[level] = [head.val]
            if head.left:
                q.append((head.left, level-1))
            if head.right:
                q.append((head.right, level+1))
        for k, v in sorted(hashmap.iteritems(), key=lambda (k,v): (k,v)):
            res.append(v)

        return res
        
