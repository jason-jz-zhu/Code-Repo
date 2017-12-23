# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findClosestLeaf(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if not root:
            return -1
        graph = collections.defaultdict(list)
        leaves = set()
        
        self.helper(root, graph, leaves)
        q = [k]
        visited = set([k])
        while q:
            next_q = []
            for node in q:
                if node in leaves:
                    return node
                for n_node in graph[node]:
                    if n_node in visited:
                        continue
                    visited.add(n_node)
                    next_q.append(n_node)
            q = next_q
        return 0
    
    def helper(self, node, graph, leaves):
        if not node:
            return 
        if not node.left and not node.right:
            leaves.add(node.val)
            return 
        if node.left:
            graph[node.val].append(node.left.val)
            graph[node.left.val].append(node.val)
            self.helper(node.left, graph, leaves)
        if node.right:
            graph[node.val].append(node.right.val)
            graph[node.right.val].append(node.val)
            self.helper(node.right, graph, leaves)
        
        
        