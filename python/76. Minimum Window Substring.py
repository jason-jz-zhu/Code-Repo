class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window, need = {}, {}
        for c in t:
            need[c] = need.get(c, 0) + 1

        left = right = 0
        valid = 0
        start = 0
        lenght = float("inf")

        while right < len(s):
            c = s[right]
            right += 1
            if c in need:
                window[c] = window.get(c, 0) + 1
                if window[c] == need[c]:
                    valid += 1
            while valid == len(need):
                if right - left < lenght:
                    start = left
                    lenght = right - left

                d = s[left]
                left += 1
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
        
        return "" if lenght == float("inf") else s[start: start + lenght]
        

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ''
        left = right = 0
        s_visited = collections.defaultdict(int)
        t_counter = collections.Counter(t)
        cnt = 0
        min_len = float('inf')
        while right < len(s):
            if s[right] in t_counter and s_visited[s[right]] < t_counter[s[right]]:
                cnt += 1
            s_visited[s[right]] += 1
            while left <= right and cnt == len(t):
                if min_len > right - left + 1:
                    min_len = right - left + 1
                    res = s[left : right + 1]
                s_visited[s[left]] -= 1
                if s[left] in t_counter and s_visited[s[left]] < t_counter[s[left]]:
                    cnt -= 1
                left += 1
            right += 1
        return res
