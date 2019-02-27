class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        if not A or len(A) == 0:
            return []

        start = end = 0
        while end < len(A):
            if A[end] % 2 == 0:
                A[start], A[end] = A[end], A[start]
                start += 1
            end += 1
        return A
