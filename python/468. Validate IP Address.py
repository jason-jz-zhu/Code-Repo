class Solution(object):
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        def is_hex(s):
            hex_digits = set("0123456789abcdefABCDEF")
            for char in s:
                if not (char in hex_digits):
                    return False
            return True
        blocks = IP.split('.')
        if len(blocks) == 4:
            for i in xrange(len(blocks)):
                if not blocks[i].isdigit() or not 0 <= int(blocks[i]) < 256 or \
                    (blocks[i][0] == '0' and len(blocks[i]) > 1):
                        return 'Neither'
            return 'IPv4'

        blocks = IP.split(':')
        if len(blocks) == 8:
            for i in xrange(len(blocks)):
                if not (1 <= len(blocks[i]) <= 4) or not is_hex(blocks[i]):
                        return 'Neither'
            return 'IPv6'

        return 'Neither'
