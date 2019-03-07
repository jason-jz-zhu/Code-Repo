# nlogn
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums or len(nums) == 0:
            return 0
        nums.sort()

        curr = 1
        longest = 0

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                continue
            if nums[i] == nums[i - 1] + 1:
                curr += 1
            else:
                longest = max(curr, longest)
                curr = 1
        return max(longest, curr)

# n
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        hashset = set(nums)
        for num in nums:
            if num - 1 not in hashset:
                curr_num = num
                curr_long = 1
                while curr_num + 1 in hashset:
                    curr_num += 1
                    curr_long += 1
                longest = max(longest, curr_long)
        return longest

# union find
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums or len(nums) == 0:
            return 0
        self.father = {num: num for num in nums}
        self.count = {num: 1 for num in nums}
        for i in range(len(nums)):
            if nums[i] + 1 in self.father:
                self.union(nums[i], nums[i] + 1)
            if nums[i] - 1 in self.father:
                self.union(nums[i], nums[i] - 1)

        return max(self.count.values())

    def find(self, node):
        if node == self.father[node]:
            return node
        self.father[node] = self.find(self.father[node])
        return self.father[node]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.father[root_x] = root_y
            self.count[root_y] += self.count[root_x]
