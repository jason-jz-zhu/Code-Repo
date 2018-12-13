class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s is None:
            return False
        hashmap = {']': '[', '}': '{', ')': '('}
        stack = []
        for c in s:
            if c in hashmap.values():
                stack.append(c)
            elif c in hashmap.keys():
                if not stack or hashmap[c] != stack.pop():
                    return False
            else:
                return False
        return stack == []
