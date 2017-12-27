# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

# interative space: o(1) one loop
class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return
        curr = dummy = TreeLinkNode(0)
        while root:
            curr.next = root.left
            if curr.next:
                curr = curr.next
            curr.next = root.right
            if curr.next:
                curr = curr.next
            root = root.next
            if not root:
                curr = dummy
                root = dummy.next

# interative space: o(1) two loop
class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return
        while root:
            curr = tmp = TreeLinkNode(0)
            while root:
                if root.left:
                    curr.next = root.left
                    curr = root.left
                if root.right:
                    curr.next = root.right
                    curr = root.right
                root = root.next
            root = tmp.next

# level order space: o(n)
class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return
        q = [root, None]
        while q:
            for i in range(len(q) - 1):
                q[i].next = q[i + 1]
            q = [kid for node in q[:-1] for kid in (node.left, node.right) if kid]
            if not q:
                break
            q.append(None)

# recursive space: o(n)
class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return
        self.helper(root.left, root.right)

    def helper(self, node1, node2):
        if not node1:
            return
        node1.next = node2
        self.helper(node1.left, node1.right)
        self.helper(node2.left, node2.right)
        self.helper(node1.right, node2.left)
