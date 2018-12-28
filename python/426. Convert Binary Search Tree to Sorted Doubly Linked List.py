"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution:
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None
        head = [None]
        prev = [None]
        self.inorder(root, prev, head)
        prev[0].right = head[0]
        head[0].left = prev[0]
        return head[0]

    def inorder(self, node, prev, head):
        if not node:
            return

        self.inorder(node.left, prev, head)

        if not head[0]:
            head[0] = node
            prev[0] = node
        else:
            prev[0].right = node
            node.left = prev[0]
            prev[0] = node

        self.inorder(node.right, prev, head)
