# hashmap
class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        hashmap = collections.defaultdict(int)
        curr_sum = 0
        res = 0
        hashmap[0] = 1
        for num in A:
            curr_sum += num
            mod = curr_sum % K
            res += hashmap[mod]
            hashmap[mod] += 1
        return res

# dp
class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        m = len(A)
        s = [0]
        for num in A:
            s.append(s[-1] + num)

        dp = [0] * (m + 1)

        for i in range(1, m + 1):
            for j in range(i - 1, -1, -1):
                if (s[i] - s[j]) % K == 0:
                    dp[i] = dp[j] + 1
                    break
        return sum(dp)
