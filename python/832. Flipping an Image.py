class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        if not A or len(A) == 0 or len(A[0]) == 0:
            return []

        m, n = len(A), len(A[0])
        for i in range(m):
            A[i] = A[i][::-1]
            for j in range(n):
                A[i][j] ^= 1
        return A
