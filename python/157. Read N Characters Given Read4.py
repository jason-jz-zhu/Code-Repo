# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        idx = 0
        while True:
            buf4 = [""] * 4
            curr = min(read4(buf4), n-idx)
            for i in xrange(curr):
                buf[idx] = buf4[i]
                idx += 1
            if curr == 0:
                break
        return idx



# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        index = 0
        buf4 = [''] * 4
        while True:
            cnt = read4(buf4)
            if cnt == 0:
                break
            i = 0
            while index < n and i < cnt:
                buf[index] = buf4[i]
                index += 1
                i += 1
        return index
