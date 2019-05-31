class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.append(0)
        m = len(nums)

        for i in range(m):
            if nums[i] < 0 or nums[i] >= m:
                nums[i] = 0

        for i in range(m):
            nums[nums[i] % m] += m

        for i in range(1, m):
            if nums[i] // m == 0:
                return i
        return m





class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        m = len(nums)
        i = 0
        while i < m:
            if nums[i] > 0 and nums[i] <= m and nums[i] - 1 != i and nums[i] != nums[nums[i] - 1]:
                nums[i], nums[nums[i] - 1] = nums[i], nums[nums[i] - 1]
            else:
                i += 1
        for i in range(m):
            if nums[i] - 1 != i:
                return i + 1
        return m + 1
