def sum13(nums):
  if nums is None or len(nums) == 0:
    return 0

  res = 0
  if nums[0] != 13:
    res += nums[0]

  for i in xrange(1, len(nums)):
    if nums[i] == 13 or nums[i-1] == 13:
      continue
    res += nums[i]
  return res
