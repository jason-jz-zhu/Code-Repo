class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:

        s = []
        for i in range(len(nums)):
            for num in nums[i]:
                s.append((num, i))
        s.sort()

        res = []
        left = right = 0
        min_len = float('inf')
        cnt = 0
        visited = collections.defaultdict(int)
        while right < len(s):
            if visited[s[right][1]] == 0:
                cnt += 1
            visited[s[right][1]] += 1
            while left <= right and cnt == len(nums):
                if min_len > s[right][0] - s[left][0]:
                    min_len = s[right][0] - s[left][0]
                    res = [s[left][0], s[right][0]]
                visited[s[left][1]] -= 1
                if visited[s[left][1]] == 0:
                    cnt -= 1
                left += 1
            right += 1
        return res



class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        heap = [(arr[0], i, 0) for i, arr in enumerate(nums)]
        heapq.heapify(heap)
        max_val = max([arr[0] for arr in nums])
        res = (float('-inf'), float('inf'))
        while heap:
            min_val, list_index, num_index = heapq.heappop(heap)
            if max_val - min_val < res[1] - res[0]:
                res = (min_val, max_val)
            if num_index == len(nums[list_index]) - 1:
                return res

            next_num = nums[list_index][num_index + 1]
            max_val = max(max_val, next_num)
            heapq.heappush(heap, (next_num, list_index, num_index + 1))
