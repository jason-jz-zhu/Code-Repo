class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        res = set()
        for email in emails:
            local, domain = email.split('@')
            tmp = ''
            for c in local:
                if c == '+':
                    break
                elif c != '.':
                    tmp += c
            res.add(tmp + '@' + domain)
        return len(res)
                
