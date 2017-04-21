class Solution:
    # @param {double} x a double
    # @return {double} the square root of x
    def sqrt(self, x):
        # Write your code here
        start = 0.0
        end = x
        eps = 1e-12

        if x < 1.0:
            end = 1.0

        while end - start > eps:
            mid = (end - start) / 2 + start
            if mid * mid < x:
                start = mid
            else:
                end = mid

        return start
