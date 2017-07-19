def count_hi(str):
  res = 0
  for i in xrange(len(str) - 1):
    if str[i:i+2] == 'hi':
      res += 1
  return res
