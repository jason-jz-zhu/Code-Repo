
# stable
# Time: O(nlog(n))
# Space: O(n)

nums = [4, 3, 5, 2, 1]

def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    l = len(nums) // 2
    left = merge_sort(nums[:l])
    right = merge_sort(nums[l:])
    return merge(left, right)

def merge(left, right):
    i = j = 0
    res = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    res += left[i:] or right[j:]
    return res

print(merge_sort(nums))
