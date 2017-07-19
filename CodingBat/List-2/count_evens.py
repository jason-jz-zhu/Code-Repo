def count_evens(nums):
  res = 0
  for num in nums:
    if num % 2 == 0:
      res += 1
  return res
