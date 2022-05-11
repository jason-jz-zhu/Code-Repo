class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        if not logs or len(logs) == 0:
            return -1
        
        logs.sort(key = lambda x: x[0])
        
        parents = [i for i in range(n)]
        ranks = [1 for _ in range(n)]
        cnt = n
        def find(u):
            if parents[u] == u:
                return u
            parents[u] = find(parents[u])
            return parents[u]
        
        def union(u, v):
            nonlocal cnt
            pu, pv = find(u), find(v)
            if pu == pv:
                return False
            if ranks[pu] < ranks[pv]:
                parents[pu] = pv
            elif ranks[pu] > ranks[pv]:
                parents[pv] = pu
            else:
                parents[pv] = pu
                ranks[pu] += 1
            cnt -= 1
            return True
        
        for tm, u, v in logs:
            union(u, v)
            if cnt == 1:
                return tm
        return -1
