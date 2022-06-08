class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for s in strings:
            key = ()
            for i in range(len(s) - 1):
                tmp = 26 + ord(s[i + 1]) - ord(s[i])
                key += (tmp % 26,)
            hashmap[key].append(s)
        return list(hashmap.values())
