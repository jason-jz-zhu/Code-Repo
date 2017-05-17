# nlog(n)
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort(reverse=True)
        return nums[k-1]

# O(k+(n-k)lgk) time, min-heap
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        import heapq
        # init heap
        heap = []
        # push num into heap
        for num in nums:
            heapq.heappush(heap, num)
        # pop num until len(nums) - k
        for _ in xrange(len(nums) - k):
            heapq.heappop(heap)
        # return the largets k
        return heapq.heappop(heap)

# O(k+(n-k)lgk) time, min-heap
def findKthLargest5(self, nums, k):
    return heapq.nlargest(k, nums)[k-1]

# O(nk) time, bubble sort idea
def findKthLargest(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    for i in xrange(k):
        for j in xrange(len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    # return value
    return nums[len(nums) - k]

# O(nk) time, selection sort idea
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        for i in xrange(len(nums), len(nums) - k, -1):
            temp = 0
            for j in xrange(i):
                if nums[j] > nums[temp]:
                    temp = j
            nums[temp], nums[i - 1] = nums[i - 1], nums[temp]
        return nums[len(nums) - k]
        
# O(n) time, quick selection
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return self.findKthSmallest(nums, len(nums) - k + 1)

    def findKthSmallest(self, nums, i):
        if nums:
            pos = self.partition(nums, 0, len(nums) - 1)
            if i - 1 > pos:
                return self.findKthSmallest(nums[pos+1:], i - pos - 1)
            elif i - 1 < pos:
                return self.findKthSmallest(nums[:pos], i)
            else:
                return nums[pos]

    def partition(self, nums, l, r):
        low = l
        while l < r:
            if nums[l] < nums[r]:
                nums[low], nums[l] = nums[l], nums[low]
                low += 1
            l += 1
        nums[low], nums[r] = nums[r], nums[low]
        return low
