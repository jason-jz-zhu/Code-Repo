class Solution(object):
    def sequenceReconstruction(self, org, seqs):
        """
        :type org: List[int]
        :type seqs: List[List[int]]
        :rtype: bool
        """
        if seqs is None or len(seqs) == 0:
            return False
        indegree = {}
        graph = {}
        res = []
        for seq in seqs:
            for d in seq:
                if d not in graph:
                    indegree[d] = 0
                    graph[d] = set()

        for seq in seqs:
            for i in range(1, len(seq)):
                if seq[i] not in graph[seq[i - 1]]:
                    indegree[seq[i]] += 1
                graph[seq[i - 1]].add(seq[i])

        q = collections.deque([i for i in indegree if indegree[i] == 0])

        while q:
            if len(q) != 1:
                return False
            curr_node = q.popleft()
            res.append(curr_node)
            for node in graph[curr_node]:
                indegree[node] -= 1
                if indegree[node] == 0:
                    q.append(node)
        if len(res) != len(graph):
            return False
        if res == org:
            return True
        return False
