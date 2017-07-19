def centered_average(nums):
  sort_num = sorted(nums)
  cut_num = sort_num[1:-1]
  return int(sum(cut_num) / len(cut_num))
