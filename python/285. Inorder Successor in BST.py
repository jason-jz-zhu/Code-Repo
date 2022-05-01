# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# o(h) o (1)
class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        ans = None
        while root:
            if root.val <= p.val:
                root = root.right
            else:
                ans = root
                root = root.left
        return ans

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val <= p.val:
            return self.inorderSuccessor(root.right, p)
        else:
            ans = self.inorderSuccessor(root.left, p)
            return ans if ans else root
    
    
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

    
class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        if not root:
            return None
        self.ans = None
        self.find = False
        self.dfs(root, p)
        return self.ans
        
    def dfs(self, root, p):
        if not root:
            return 
        self.dfs(root.left, p)
        
        if self.find and not self.ans:
            self.ans = root
            return 
        if root.val == p.val:
            self.find = True
        
        self.dfs(root.right, p)
