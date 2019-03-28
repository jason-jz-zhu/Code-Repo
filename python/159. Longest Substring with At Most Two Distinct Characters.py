class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        res = 0
        left = right = 0
        visited = collections.defaultdict(int)
        while right < len(s):
            visited[s[right]] += 1
            while left <= right and len(visited) > 2:
                visited[s[left]] -= 1
                if visited[s[left]] == 0:
                    del visited[s[left]]
                left += 1

            res = max(res, right - left + 1)
            right += 1
        return res

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:

        left = right = 0
        res = 0
        visited = collections.defaultdict(int)
        while right < len(s):
            if (s[right] not in visited and len(visited) < 2) or (s[right] in visited and len(visited) <= 2):
                res = max(res, right - left + 1)
                visited[s[right]] += 1
                right += 1
            else:
                visited[s[left]] -= 1
                if visited[s[left]] == 0:
                    del visited[s[left]]
                left += 1
        return res
