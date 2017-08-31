# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return False


class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        import collections
        queue = collections.deque([])
        queue.append((p, q))
        while queue:
            cur1, cur2 = queue.popleft()
            if not cur1 and not cur2:
                continue
            elif not cur1 or not cur2:
                return False
            else:
                if cur1.val != cur2.val:
                    return False
                queue.append((cur1.left, cur2.left))
                queue.append((cur1.right, cur2.right))
        return True
