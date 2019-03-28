class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        size1, size2 = len(s1), len(s2)
        counter1 = collections.Counter(s1)
        counter2 = collections.Counter(s2[: size1])
        if counter1 == counter2:
            return True

        for i in range(size1, size2):
            counter2[s2[i]] += 1
            counter2[s2[i - size1]] -= 1
            if counter2[s2[i - size1]] == 0:
                del counter2[s2[i - size1]]
            if counter1 == counter2:
                return True
        return False
