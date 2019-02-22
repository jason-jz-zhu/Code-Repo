class Solution:
    def alienOrder(self, words: 'List[str]') -> 'str':
        indegree = {}
        graph = {}

        for i in range(len(words)):
            for j in range(len(words[i])):
                key = ord(words[i][j]) - ord('a')
                indegree[key] = 0
                graph[key] = set()

        for i in range(1, len(words)):
            w1 = words[i - 1]
            w2 = words[i]
            for j in range(min(len(w1), len(w2))):
                if w1[j] != w2[j]:
                    j1 = ord(w1[j]) - ord('a')
                    j2 = ord(w2[j]) - ord('a')
                    if j2 not in graph[j1]:
                        indegree[j2] += 1
                    graph[j1].add(j2)
                    break
        res = ''
        q = collections.deque([i for i in indegree if indegree[i] == 0])
        while q:
            curr_node = q.popleft()
            res += chr(curr_node + ord('a'))
            for node in graph[curr_node]:
                indegree[node] -= 1
                if indegree[node] == 0:
                    q.append(node)

        if len(res) == len(indegree):
            return res
        return ''
        
