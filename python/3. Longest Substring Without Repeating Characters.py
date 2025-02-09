class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = right = 0
        windows = {}
        res = 0
        while right < len(s):
            c = s[right]
            right += 1
            windows[c] = 1 if c not in windows else windows[c] + 1
            # windows[c] = windows.get(c, 0) + 1
            while windows[c] > 1:
                d = s[left]
                left += 1
                windows[d] -= 1

            res = max(res, right - left)

        return res

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


# Pseudocode framework for sliding window algorithm
def slidingWindow(s: str):
    # Use an appropriate data structure to record the data
    # in the window, which can vary depending on the
    # For example, if I want to record the
    # frequency of elements in the window, I would
    # If I want to record the sum of elements in the window, I could just use an int
    window = ...

    left, right = 0, 0
    while right < len(s):
        # c is the character that will be added to the window
        c = s[right]
        window.add(c)
        # Expand the window
        right += 1
        # Perform a series of updates on the data within the window
        ...

        # *** position for debug output ***
        # Note that you should not print in the final solution code
        # because IO operations are time-consuming and may cause timeouts
        # print(f"window: [{left}, {right})")
        # ***********************

        # Determine whether the left side of the window needs to be contracted
        while left < right and window needs shrink:
            # d is the character that will be removed from the window
            d = s[left]
            window.remove(d)
            # Shrink the window
            left += 1
            # Perform a series of updates on the data within the window
            ...