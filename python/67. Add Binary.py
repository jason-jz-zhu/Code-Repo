class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        idx_a, idx_b = len(a) - 1, len(b) - 1
        ans = ''
        while idx_a >= 0 or idx_b >= 0:
            if idx_a >= 0:
                carry += int(a[idx_a])
                idx_a -= 1
            if idx_b >= 0:
                carry += int(b[idx_b])
                idx_b -= 1
            
            reminder = carry % 2
            carry //= 2
            ans = str(reminder) + ans
        if carry:
            ans = str(carry) + ans
        return ans
            
