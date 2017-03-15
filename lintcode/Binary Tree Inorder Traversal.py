
# traverse
class Solution:
    """
    @param root: The root of binary tree.
    @return: Preorder in ArrayList which contains node values.
    """

    def inorderTraversal(self, root):
        # write your code here
        res = []
        self.traverse(root, res)
        return res

    def traverse(self, root, res):
        if root is None:
            return
        self.traverse(root.left, res)
        res.append(root.val)
        self.traverse(root.right, res)

# using stack
class Solution:
    """
    @param root: The root of binary tree.
    @return: Inorder in ArrayList which contains node values.
    """
    def inorderTraversal(self, root):
        # write your code here
        res = []
        stack = []
        p = root
        while stack or p:
            while p:
                stack.append(p)
                p = p.left
            p = stack.pop()
            res.append(p.val)
            p = p.right
        return res
