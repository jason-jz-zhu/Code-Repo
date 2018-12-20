
# non-stable
# Time: O(nlog(n))
# Space: None

nums = [4, 3, 5, 2, 1]


def selection_sort(nums):
    for i in range(len(nums)):
        mv = i
        for j in range(i + 1, len(nums)):
            if nums[mv] > nums[j]:
                mv = j
        nums[mv], nums[i] = nums[i], nums[mv]
    return nums



print(selection_sort(nums))
