def lone_sum(a, b, c):
  args = [a , b, c]
  return sum(v for v in args if args.count(v) == 1)
