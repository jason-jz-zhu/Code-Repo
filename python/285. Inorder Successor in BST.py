class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        if root is None or p is None:
            return None

        found_p = False
        stack = []
        while root is not None or stack:
            if root is not None:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                if found_p:
                    return root
                if root.val == p.val:
                    found_p = True
                root = root.right

        return None
