# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''

        def dfs(root):
            if not root:
                res.append('#null')
                return
            res.append('#' + str(root.val))
            dfs(root.left)
            dfs(root.right)

        res = []
        dfs(root)
        return ''.join(res)


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data is None or len(data) == 0:
            return None

        def dfs():
            val = next(data_list)
            if val == 'null':
                return None
            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()
            return node

        data_list = iter(data[1:].split('#'))

        return dfs()


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
