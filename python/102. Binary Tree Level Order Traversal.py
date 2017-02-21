# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        q = []
        q.append(root)
        result = []
        while q:
            tempResult = []
            temp = q
            q = []
            for ele in temp:
                if ele: tempResult.append(ele.val)
                if ele.left: q.append(ele.left)
                if ele.right: q.append(ele.right)
            result.append(tempResult)
        return result