
# stable
# Time: O(n^2)
# Space: None


nums = [4, 3, 5, 2, 1]

def insert_sort(nums):
    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1
        while j >= 0:
            if nums[j] > key:
                nums[j + 1], nums[j] = nums[j], key
            j -= 1
    return nums

print(insert_sort(nums))
