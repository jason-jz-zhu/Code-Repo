class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        return self.get_number_at_most_k(A, K) - self.get_number_at_most_k(A, K - 1)

    def get_number_at_most_k(self, A, K):
        res = 0
        left = right = 0
        visited = collections.defaultdict(int)
        while right < len(A):
            visited[A[right]] += 1
            while left <= right and len(visited) > K:
                visited[A[left]] -= 1
                if visited[A[left]] == 0:
                    del visited[A[left]]
                left += 1
            res += right - left + 1
            right += 1
        return res
