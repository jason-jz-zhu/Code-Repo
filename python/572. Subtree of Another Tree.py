class Solution:
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if not s or not t:
            return False
        t1 = self.helper(s)
        t2 = self.helper(t)
        print(t1)
        print(t2)
        if t2 in t1:
            return True
        return False

    def helper(self, root):
        res = []
        self.dfs(root, res)
        return ''.join(res)

    def dfs(self, root, res):
        if not root:
            res.append('#null')
            return
        res.append('#{}'.format(str(root.val)))
        self.dfs(root.left, res)
        self.dfs(root.right, res)

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        t1 = self.preorder(s, True)
        t2 = self.preorder(t, True)
        if t2 in t1:
            return True
        return False

    def preorder(self, t, left):
        if not t:
            if left:
                return 'lnull'
            else:
                return 'rnull'

        return '#' + str(t.val) + self.preorder(t.left, True) + self.preorder(t.right, False)



class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if not s:
            return False

        if self.helper(s, t):
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def helper(self, s, t):
        if not s and not t:
            return True
        if not s or not t:
            return False
        if s.val != t.val:
            return False
        return self.helper(s.left, t.left) and self.helper(s.right, t.right)
