# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        if not root:
            return None
        res = root.val
        while root:
            res = res if abs(res - target) < abs(root.val - target) else root.val
            root = root.left if target < root.val else root.right
        return res

class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        
        def dfs(node):
            nonlocal ans
            if not node:
                return
            ans = ans if abs(target - ans) < abs(target - node.val) else node.val
            if target < node.val:
                dfs(node.left)
            else:
                dfs(node.right)
        
        if not root:
            return -1
        ans = root.val
        dfs(root)
        return ans
    
    
    
class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        if not root:
            return None
        kid = root.left if target < root.val else root.right
        if not kid:
            return root.val
        k = self.closestValue(kid, target)
        return k if abs(k - target) < abs(root.val - target) else root.val
