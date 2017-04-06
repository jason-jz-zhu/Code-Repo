class Solution:
    """
    @param key: A String you should hash
    @param HASH_SIZE: An integer
    @return an integer
    """
    def hashCode(self, key, HASH_SIZE):
        # write your code here
        res = 0
        for k in key:
            res = (res * 33 + ord(k)) % HASH_SIZE
        return res
