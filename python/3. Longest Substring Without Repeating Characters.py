class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = collections.defaultdict(int)
        left = right = 0
        res=  0
        while right < len(s):
            visited[s[right]] += 1
            while left <= right and visited[s[right]] > 1:
                visited[s[left]] -= 1
                if visited[s[left]] == 0:
                    del visited[s[left]]
                left += 1
            res = max(res, right - left + 1)
            right += 1
        return res


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        right = 0
        visited = set()
        for left in range(len(s)):
            while right < len(s):
                if s[right] not in visited:
                    res = max(res, right - left + 1)
                    visited.add(s[right])
                    right += 1
                else:
                    break
            visited.remove(s[left])
        return res


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = right = 0
        res = 0
        visited = set()
        while right < len(s):
            if s[right] not in visited:
                res = max(res, right - left + 1)
                visited.add(s[right])
                right += 1
            else:
                visited.remove(s[left])
                left += 1
        return res
