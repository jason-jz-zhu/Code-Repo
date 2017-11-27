class Solution(object):
    def removeComments(self, source):
        """
        :type source: List[str]
        :rtype: List[str]
        """
        if source is None or len(source) == 0:
            return []

        res, buf, comment_open = [], '', False

        for line in source:
            i = 0
            while i < len(line):
                s = line[i]
                # //
                if (i + 1) < len(line) and line[i: i + 2] == '//' and not comment_open:
                    i = len(line)
                # /*
                elif (i + 1) < len(line) and line[i: i + 2] == '/*' and not comment_open:
                    i += 1
                    comment_open = True
                # */
                elif (i + 1) < len(line) and line[i: i + 2] == '*/' and comment_open:
                    i += 1
                    comment_open = False
                elif not comment_open:
                    buf += s
                i += 1
            if buf and not comment_open:
                res.append(buf)
                buf = ''
        return res
