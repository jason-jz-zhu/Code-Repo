class Solution(object):
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        if IP is None or len(IP) == 0:
            return 'Neither'

        blocks = IP.split('.')
        if len(blocks) == 4:
            for i in range(len(blocks)):
                if not blocks[i].isdigit() or not 0 <= int(blocks[i]) <= 255 or \
                    (blocks[i][0] == '0' and len(blocks[i]) > 1):
                    return 'Neither'
            return 'IPv4'

        blocks = IP.split(':')
        if len(blocks) == 8:
            for i in range(len(blocks)):
                if not self.is_hex(blocks[i]) or not 1 <= len(blocks[i]) <= 4:
                    return 'Neither'
            return 'IPv6'

        return 'Neither'

    def is_hex(self, s):
        hex_digits = set("0123456789abcdefABCDEF")
        for char in s:
            if not (char in hex_digits):
                return False
        return True
