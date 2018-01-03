class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s:
            return True

        i = 0
        for c in t:
            if s[i] == c:
                i += 1
            if i == len(s):
                break
        return i == len(s)

# follow up
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s is None or len(s) == 0:
            return True
        if t is None or len(t) == 0:
            return False
        hashmap = collections.defaultdict(list)
        for i, v in enumerate(t):
            hashmap[v].append(i)
        prev = -1
        for ss in s:
            if ss not in hashmap:
                return False
            else:
                tmp = hashmap[ss]
                prev = self.binary_search(prev, tmp, 0, len(tmp) - 1)
                if prev == -1:
                    return False
                prev += 1
        return True

    def binary_search(self, target, cache, start, end):
        while start + 1 < end:
            mid = start + (end - start) / 2
            if cache[mid] < target:
                start = mid
            else:
                end = mid
        if cache[start] >= target:
            return cache[start]
        elif cache[end] >= target:
            return cache[end]
        else:
            return -1
