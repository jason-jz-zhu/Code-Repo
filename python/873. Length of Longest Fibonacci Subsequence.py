class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        n = len(A)
        dp = collections.defaultdict(lambda: 2)
        res = 0
        hashmap = {}
        for i in range(n):
            hashmap[A[i]] = i

        for j in range(n):
            for k in range(j + 1, n):
                a_i = A[k] - A[j]
                if a_i >= A[j]:
                    break
                elif a_i not in hashmap:
                    continue
                dp[j, k] = dp[hashmap[a_i], j] + 1
                res = max(res, dp[j, k])
        return res
