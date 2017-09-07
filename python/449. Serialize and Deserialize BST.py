# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        def doit(node):
            if node:
                vals.append(str(node.val))
                doit(node.left)
                doit(node.right)
            else:
                vals.append('#')
        vals = []
        doit(root)
        return ' '.join(vals)

    def deserialize(self, data):
        def doit():
            val = next(vals)
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = doit()
            node.right = doit()
            return node
        vals = iter(data.split())
        return doit()


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        def preorder(node, vals):
            if node:
                vals.append(node.val)
                preorder(node.left, vals)
                preorder(node.right, vals)

        vals = []
        preorder(root, vals)
        return ' '.join(map(str, vals))

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        def helper(minVal, maxVal, vals):
            if not vals:
                return None
            if minVal < vals[0] < maxVal:
                val = vals.popleft()
                node = TreeNode(val)
                node.left = helper(minVal, val, vals)
                node.right = helper(val, maxVal, vals)
                return node
            else:
                return None

        vals = collections.deque([int(val) for val in data.split()])
        return helper(float('-inf'), float('inf'), vals)


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        def preorder(node, vals):
            if node:
                vals.append(node.val)
                preorder(node.left, vals)
                preorder(node.right, vals)

        vals = []
        preorder(root, vals)
        return ' '.join(map(str, vals))

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        preorder = map(int, data.split())
        inorder = sorted(preorder)

        return self.buildTree(preorder, inorder)

    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not inorder: return None # inorder is empty
        root = TreeNode(preorder[0])
        rootPos = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1 : 1 + rootPos], inorder[ : rootPos])
        root.right = self.buildTree(preorder[rootPos + 1 : ], inorder[rootPos + 1 : ])
        return root
