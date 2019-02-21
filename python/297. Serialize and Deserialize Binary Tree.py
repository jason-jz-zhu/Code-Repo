class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        def preorder(node, res):
            if node:
                res.append(node.val)
                preorder(node.left, res)
                preorder(node.right, res)
            else:
                res.append('#')

        res = []
        preorder(root, res)
        return ' '.join(map(str, res))


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        def dfs(q):
            if not q:
                return None
            val = q.popleft()
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = dfs(q)
            node.right = dfs(q)
            return node

        q = collections.deque(data.split())
        return dfs(q)
