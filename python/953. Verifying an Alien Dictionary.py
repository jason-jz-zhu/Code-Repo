class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        hashmap = {c: i for i, c in enumerate(order)}
        for i in range(len(words) - 1):
            first = words[i]
            second = words[i + 1]
            l = min(len(first), len(second))
            for j in range(l):
                if hashmap[first[j]] < hashmap[second[j]]:
                    break
                elif hashmap[first[j]] > hashmap[second[j]]:
                    return False
            if len(first) > len(second) and first[: l] == second:
                return False
        return True
