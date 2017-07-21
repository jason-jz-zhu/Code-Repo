def caught_speeding(speed, is_birthday):
  level1, level2 = 60, 80

  if is_birthday:
    level1 += 5
    level2 += 5

  if speed <= level1:
    return 0
  elif speed <= level2:
    return 1
  return 2
