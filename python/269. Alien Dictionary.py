class Solution:
    def alienOrder(self, words: 'List[str]') -> 'str':
        indegree = [-1 for _ in range(26)]
        graph = {}

        for i in range(len(words)):
            for j in range(len(words[i])):
                key = ord(words[i][j]) - ord('a')
                indegree[key] = 0
                graph[key] = []

        for i in range(1, len(words)):
            w1 = words[i - 1]
            w2 = words[i]
            for j in range(min(len(w1), len(w2))):
                if w1[j] != w2[j]:
                    j1 = ord(w1[j]) - ord('a')
                    j2 = ord(w2[j]) - ord('a')
                    indegree[j2] += 1
                    graph[j1].append(j2)
                    break

        word_cnt = len([d for d in indegree if d != -1])
        res = ''
        q = collections.deque([i for i in range(len(indegree)) if indegree[i] == 0])
        print(indegree)
        while q:
            curr_node = q.popleft()
            res += chr(curr_node + ord('a'))
            for node in graph[curr_node]:
                indegree[node] -= 1
                if indegree[node] == 0:
                    q.append(node)

        if len(res) == word_cnt:
            return res
        return ''
        
