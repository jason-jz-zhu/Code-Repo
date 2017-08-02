
class Solution(object):
    def splitArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 7:
            return False

        runSum = [0] * len(nums)
        runSum[0] = nums[0]
        for i in xrange(len(nums)):
            runSum[i] = nums[i] + runSum[i - 1]

        for j in xrange(3, len(nums)- 3):
            lookup = set()
            for i in xrange(1, j - 1):
                if runSum[i - 1] == runSum[j - 1] - runSum[i]:
                    lookup.add(runSum[i - 1])
            for k in xrange(j + 2, len(nums) - 1):
                if runSum[-1] - runSum[k] == runSum[k - 1] - runSum[j] and \
                    runSum[k - 1] - runSum[j] in lookup:
                        return True
        return False

                
