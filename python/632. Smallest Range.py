class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        s = []
        for i in range(len(nums)):
            for num in nums[i]:
                s.append((num, i))
        s.sort()
        left = right = 0
        cnt = 0
        res = []
        minLen = float('inf')
        counter = collections.defaultdict(int)
        while right < len(s):
            if counter[s[right][1]] == 0:
                cnt += 1
            counter[s[right][1]] += 1
            while left <= right and cnt == len(nums):
                if minLen > s[right][0] - s[left][0]:
                    minLen = s[right][0] - s[left][0]
                    res = [s[left][0], s[right][0]]
                counter[s[left][1]] -= 1
                if counter[s[left][1]] == 0:
                    cnt -=1
                left += 1
            right += 1
        return res
