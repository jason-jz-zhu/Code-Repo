class Larger(str):
    def __lt__(self, other):
        return self + other > other + self

class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if nums is None or len(nums) == 0:
            return ''

        tmp = [str(num) for num in nums]
        tmp.sort(key=Larger)
        largest = ''.join(tmp)
        return '0' if largest[0] == '0' else largest
