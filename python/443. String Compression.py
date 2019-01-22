class Solution:
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        if chars is None or len(chars) == 0:
            return 0

        cnt = 1
        end = 0
        for i in range(1, len(chars) + 1):
            if i != len(chars) and chars[i] == chars[i - 1]:
                cnt += 1
            else:
                chars[end] = chars[i - 1]
                end += 1
                if cnt != 1:
                    list_int = list(str(cnt))
                    for d in list_int:
                        chars[end] = d
                        end += 1
                cnt = 1
        return end
