class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        q = []
        for u, v, w in pipes:
            q.append((w, u, v))
        for i, cost in enumerate(wells):
            q.append((cost, 0, i + 1))
        q.sort()
        
        parents = [i for i in range(n + 1)]
        ranks = [1 for _ in range(n + 1)]
        
        def find(u):
            if parents[u] == u:
                return u
            parents[u] = find(parents[u])
            return parents[u]
        
        def union(u, v):
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
            return True
        res = 0
        count = 0
        for w, u, v in q:
            rA, rB = find(u), find(v)
            if rA == rB:
                continue
            union(rA, rB)
            res += w
            # Optimize so that we don't traverse all edges
            count += 1
            if count == n:
                return res
        return res 
