def sum67(nums):
  if nums is None or len(nums) == 0:
    return 0

  total = 0
  found6 = False

  for i in range(len(nums)):
      if nums[i] == 6:
          found6 = True
      if not found6:
          total += nums[i]
      if nums[i] == 7 and found6:
          found6 = False

  return total
