
# non-stable
# Time: O(nlog(n))
# Space: None

nums = [4, 3, 5, 2, 1]


def quick_sort(nums, left, right):
    if left < right:
        q = partition(nums, left, right)
        quick_sort(nums, left, q - 1)
        quick_sort(nums, q + 1, right)

def partition(nums, left, right):
    k = nums[right]
    i = left - 1
    for j in range(left, right):
        if nums[j] <= k:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
    nums[i + 1], nums[right] = nums[right], nums[i + 1]
    return i + 1

quick_sort(nums, 0, len(nums) - 1)
print(nums)
