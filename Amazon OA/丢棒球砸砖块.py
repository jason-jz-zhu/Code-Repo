def ballCount(scores):
    res = 0
    stack = []
    for score in scores:
        # clear pre one element
        if score == 'Z':
            if stack:
                val = stack.pop()
                res -= val
            else:
                print 'error Z'
        # current score is double pre one
        elif score == 'X':
            if stack:
                val = 2 * stack.pop()
                res += val
                stack.append(val)
            else:
                print 'error X'
        elif score == '+':
            if len(stack) >= 2:
                val = stack[-1] + stack[-2]
                res += val
                stack.append(val)
            else:
                print 'error +'
        else:
            val = int(score)
            res += val
            stack.append(val)
    return res

print ballCount([5, -2, 4, 'Z', 'X', 9, '+', '+'])
