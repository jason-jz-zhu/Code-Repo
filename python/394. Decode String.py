class Solution:
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s is None or len(s) == 0:
            return ''
        stack = []
        curr_num = 0
        curr_str = ''
        for c in s:
            if c.isdigit():
                curr_num = curr_num * 10 + int(c)
            elif c == '[':
                stack.append(curr_str)
                stack.append(curr_num)
                curr_str = ''
                curr_num = 0
            elif c == ']':
                prev_num = stack.pop()
                prev_str = stack.pop()
                curr_str = prev_str + prev_num * curr_str
            else:
                curr_str += c
        return curr_str
