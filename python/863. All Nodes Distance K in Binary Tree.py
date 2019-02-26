# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        graph = collections.defaultdict(list)
        self.build_graph(None, root, graph)
        q = [target]
        visited = [target]
        res = []
        level = 0
        while q:
            if level == K:
                res = [node.val for node in q]
                break
            visited += q
            q = [child for node in q for child in graph[node] if child not in visited]
            level += 1

        return res

    def build_graph(self, parent, child, graph):
        if parent:
            graph[parent].append(child)
            graph[child].append(parent)
        if child.left:
            self.build_graph(child, child.left, graph)
        if child.right:
            self.build_graph(child, child.right, graph)


class Solution:
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        graph = collections.defaultdict(list)
        self.build_graph(None, root, graph)
        q = [target]
        visited = set([target])
        res = []

        for _ in range(K):
            q = [child for node in q for child in graph[node] if child not in visited]
            visited |= set([node for node in q])
        return [node.val for node in q]
