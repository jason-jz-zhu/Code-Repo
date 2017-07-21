def cat_dog(str):
  c_cnt = d_cnt = 0
  for i in xrange(len(str) - 2):
    if str[i:i+3] == 'cat':
      c_cnt += 1
    if str[i:i+3] == 'dog':
      d_cnt += 1

  return c_cnt == d_cnt
