def big_diff(nums):
  min_val = max_val = nums[0]
  for i in xrange(1, len(nums)):
    if nums[i] < min_val:
      min_val = nums[i]
    if nums[i] > max_val:
      max_val = nums[i]
  return abs(max_val - min_val)
