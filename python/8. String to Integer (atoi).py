class Solution:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0
        s = s.strip()
        if len(s) == 0:
            return 0
        
        res = 0
        sign = 1
        i = 0
        if s[i] == "+":
            i += 1
        elif s[i] == "-":
            sign = -1
            i += 1
        for j in range(i, len(s)):
            if not s[j].isdigit():
                break
            res = res * 10 + int(s[j])
            if res > float("inf"):
                break
        res *= sign
        if res >= 2 ** 31:
            return 2 ** 31 - 1
        if res <= -2 ** 31:
            return -2 ** 31
        return res