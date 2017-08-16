class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s is None or len(s) == 0:
            return ''
        n = 0
        curr, nums, strs = [], [], []

        for c in s:
            if c.isdigit():
                n = n * 10 + ord(c) - ord('0')
            elif c == '[':
                nums.append(n)
                n = 0
                strs.append(curr)
                curr = []
            elif c == ']':
                strs[-1].extend(curr * nums.pop())
                curr = strs.pop()
            else:
                curr.append(c)

        return "".join(curr)
