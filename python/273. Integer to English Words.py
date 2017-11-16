class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        LESS_THAN_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", \
        "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", \
        "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        TENS = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        THOUSANDS = ["", "Thousand", "Million", "Billion"]

        def helper(num):
            if num == 0:
                return ''
            elif num < 20:
                return LESS_THAN_20[num] + ' '
            elif num < 100:
                return TENS[num / 10] + ' ' + helper(num % 10)
            else:
                return LESS_THAN_20[num / 100] + ' Hundred ' + helper(num % 100)

        if num == 0:
            return 'Zero'
        level, res = 0, ''

        while num > 0:
            if num % 1000 != 0:
                res = helper(num % 1000) + THOUSANDS[level] + ' ' + res
            num /= 1000
            level += 1

        return res.strip()
