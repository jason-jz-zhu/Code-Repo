# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param {UndirectedGraphNode[]} graph a list of undirected graph node
    # @param {dict} values a dict, <UndirectedGraphNode, (int)value>
    # @param {UndirectedGraphNode} node an Undirected graph node
    # @param {int} target an integer
    # @return {UndirectedGraphNode} a node
    def searchNode(self, graph, values, node, target):
        # Write your code here
        q = collections.deque([node])
        h = {node: True}
        while q:
            head = q.popleft()
            if values.get(head) == target:
                return head
            for item in head.neighbors:
                if not h.get(item):
                    q.append(item)
                    h[item] = True
        return None
