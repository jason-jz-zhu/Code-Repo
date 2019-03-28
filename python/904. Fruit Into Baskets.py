class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        left = right = 0
        visited = collections.defaultdict(int)
        res = float('-inf')
        while right < len(tree):
            visited[tree[right]] += 1
            while left <= right and len(visited) > 2:
                visited[tree[left]] -= 1
                if visited[tree[left]] == 0:
                    del visited[tree[left]]
                left += 1
            res = max(res, right - left + 1)
            right += 1
        return res
