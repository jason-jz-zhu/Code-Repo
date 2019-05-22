class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        if wordlist is None or len(wordlist) == 0:
            return []

        orig = {}
        low = {}
        vow = {}
        for w in wordlist:
            orig[w] = w
            l = w.lower()
            if l not in low:
                low[l] = w
            v = re.sub(r'[aeiou]', '*', l)
            if v not in vow:
                vow[v] = w

        res = []
        for q in queries:
            if q in orig:
                res.append(q)
                continue
            l = q.lower()
            if l in low:
                res.append(low[l])
                continue
            v = re.sub(r'[aeiou]', '*', l)
            if v in vow:
                res.append(vow[v])
                continue
            res.append('')

        return res
