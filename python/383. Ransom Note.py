class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        if ransomNote is None or len(ransomNote) == 0:
            return True
        if magazine is None:
            return False
        hashmap = collections.Counter(ransomNote)
        for m in magazine:
            if m in hashmap:
                hashmap[m] -= 1
                if hashmap[m] == 0:
                    del hashmap[m]
        return len(hashmap) == 0
            
