# 1）What if the given array is already sorted? How would you optimize your algorithm?
# 用two pointers 比较
#
# 2）What if nums1's size is small compared to num2's size? Which algorithm is better?
# 将nums1 的数据存进hash map，然后遍历nums2 查找是否在nums1中
#
# 3）What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
# 因为nums1是可以放到内存的，所以就把nums1放到hashmap里，然后从disk分多次取出nums2，判断一下就好了

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)

        lookup = collections.Counter(nums1)

        res = []
        for i in nums2:
            if lookup[i] > 0:
                res.append(i)
                lookup[i] -= 1
        return res

# If the given array is not sorted, and the memory is limited.
# Time:  O(max(m, n) * log(max(m, n)))
# Space: O(1)
# Two pointers solution.
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if nums1 is None or len(nums1) == 0:
            return []
        if nums2 is None or len(nums2) == 0:
            return []
        nums1, nums2 = sorted(nums1), sorted(nums2)
        res = []
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                res.append(nums1[i])
                i, j = i + 1, j + 1
        return res

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dic = dict()
        res = []
        for v in nums1:
            if v not in dic:
                # [counter in nums1, counter in nums2]
                dic[v] = [1,0]
            else:
                dic[v][0] += 1
        for v in nums2:
            if v in dic:
                dic[v][1] += 1
        for k,v in dic.items():
            # v appear in both lists
            if v[0]*v[1] > 0:
                for i in range(min(v[0],v[1])):
                    res.append(k)
        return res
