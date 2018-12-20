
# stable
# Time: O(n^2)
# Space: None

nums = [4, 3, 5, 2, 1]

def bubble_sort(nums):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    return nums


print(bubble_sort(nums))
