class Solution:
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        hashmap = collections.defaultdict(int)
        for cpdomain in cpdomains:
            cnt, domain = cpdomain.split()
            tmp = domain.split('.')
            for i in range(len(tmp)):
                hashmap['.'.join(tmp[i:])] += int(cnt)
        return ['{} {}'.format(cnt, domain) for domain, cnt in hashmap.items()]
