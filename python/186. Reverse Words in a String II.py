class Solution:
    # @param s, a list of 1 length strings, e.g., s = ['h','e','l','l','o']
    # @return nothing
    def reverseWords(self, s):
        def reverse(s, start, end):
            while start < end:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1

        reverse(s, 0, len(s) - 1)
        i = 0
        for j in xrange(len(s) + 1):
            if j == len(s) or s[j] == ' ':
                reverse(s, i, j - 1)
                i = j + 1
                
