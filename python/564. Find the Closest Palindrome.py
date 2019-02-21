class Solution:
    def nearestPalindromic(self, n: 'str') -> 'str':
        def delta(x):
            return abs(int(n) - int(x))

        s = len(n)
        candidates = [str(10 ** k + d) for k in (s - 1, s) for d in (-1, 1)]
        prev_c = n[: (s + 1) // 2]
        p = int(prev_c)
        for start in map(str, (p - 1, p, p + 1)):
            tmp = start + (start[: -1] if s % 2 else start)[::-1]
            candidates.append(tmp)

        res = None
        for candidate in candidates:
            if candidate != n:
                if res is None or delta(candidate) < delta(res) \
                or (delta(candidate) == delta(res) and int(candidate) < int(res)):
                    res = candidate
        return res
