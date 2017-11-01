class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        if chars is None or len(chars) == 0:
            return 0

        start = 0
        cnt = 1
        for end in range(1, len(chars) + 1):
            if end != len(chars) and chars[end] == chars[end - 1]:
                cnt += 1
            else:
                chars[start] = chars[end - 1]
                start += 1
                if cnt != 1:
                    arr_int = [d for d in str(cnt)]
                    for d in arr_int:
                        chars[start] = d
                        start += 1
                cnt = 1
        return start
