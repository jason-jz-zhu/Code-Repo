class Solution:
    def fullJustify(self, words: 'List[str]', max_width: 'int') -> 'List[str]':
        if not words or len(words) == 0:
            return []

        res = []
        curr = []
        char_cnt = 0
        for word in words:
            if char_cnt + len(word) + len(curr) > max_width:
                if len(curr) == 1:
                    res.append(curr[0] + ' ' * (max_width - char_cnt))
                else:
                    space = max_width - char_cnt
                    space_between_word = space // (len(curr) - 1)
                    extra_space = space % (len(curr) - 1)
                    for i in range(extra_space):
                        curr[i] += ' '
                    res.append((' ' * space_between_word).join(curr))
                curr = []
                char_cnt = 0
            curr.append(word)
            char_cnt += len(word)
        res.append(' '.join(curr) + ' ' * (max_width - char_cnt - len(curr) + 1))
        return res


class Solution:
    def fullJustify(self, words: 'List[str]', maxWidth: 'int') -> 'List[str]':
        if not words or len(words) == 0:
            return []

        res = []
        char_cnt = 0
        tmp = []
        for word in words:
            # char + length word + space
            if char_cnt + len(word) + len(tmp) <= maxWidth:
                char_cnt += len(word)
                tmp.append(word)
            else:
                if len(tmp) == 1:
                    cache = ''
                    cache += tmp[0]
                    cache += ' ' * (maxWidth - char_cnt)
                    res.append(cache)
                else:
                    space = maxWidth - char_cnt
                    even_space_number = space // (len(tmp) - 1)
                    extra_space = space % (len(tmp) - 1)
                    cache = tmp[0]
                    for i in range(1, len(tmp)):
                        if extra_space:
                            cache += ' '
                            extra_space -= 1
                        cache += ' ' * even_space_number
                        cache += tmp[i]
                    res.append(cache)
                char_cnt = len(word)
                tmp = [word]
        res.append(' '.join(tmp) + ' ' * (maxWidth - char_cnt - len(tmp) + 1))
        return res
