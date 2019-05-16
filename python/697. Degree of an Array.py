class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        if not nums or len(nums) == 0:
            return 0
        max_degree = 0
        nums_map = collections.defaultdict(list)
        for i, num in enumerate(nums):
            nums_map[num].append(i)
            max_degree = max(max_degree, len(nums_map[num]))

        return min(lst[-1] - lst[0] + 1 for num, lst in nums_map.items() if len(lst) == max_degree)
