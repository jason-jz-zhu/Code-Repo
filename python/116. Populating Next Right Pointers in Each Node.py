# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

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

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return
        while root.left:
            curr = root.left
            prev = None
            while root:
                if prev:
                    prev.next = root.left
                root.left.next = root.right
                prev = root.right
                root = root.next
            root = curr

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return
        q = collections.deque([root, None])
        while q:
            curr = q.popleft()
            if curr:
                curr.next = q[0]
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            else:
                if len(q) == 0:
                    return
                q.append(None)
