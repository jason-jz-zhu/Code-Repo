class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        hashmap = {1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", 40: "XL", \
        50: "L", 90: "XC", 100: "C", 400: "CD", 500: "D", 900: "CM", 1000: "M"}

        hashmap_sort = sorted(hashmap.keys(), reverse=True)
        res = ''
        for key in hashmap_sort:
            while num >= key:
                num -= key
                res += hashmap[key]
        return res
                
