class Solution:
    def threeSumMulti(self, A: List[int], target: int) -> int:
        MOD = 10 ** 9 + 7
        res = 0
        counter = collections.Counter(A)
        for i in range(target + 1):
            for j in range(i, target + 1):
                k = target - i - j
                if k < 0 or k > 100 or k < j:
                    continue
                if not counter[i] or not counter[j] or not counter[k]:
                    continue
                if i == j == k:
                    res += (counter[i] - 2) * (counter[i] - 1) * counter[k] // 6
                elif i == j and j != k:
                    res += counter[i] * (counter[i] - 1) // 2 * counter[k]
                elif i != j and j == k:
                    res += counter[i] * counter[j] * (counter[j] - 1) // 2
                else:
                    res += counter[i] * counter[j] * counter[k]
        return res % MOD
