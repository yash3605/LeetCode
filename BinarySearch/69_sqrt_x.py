"""
LeetCode #69: Sqrt(x)

Given a non-negative integer x, compute and return the square root of x. Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned. You are not allowed to use any built-in exponent function or operator.

Constraints:
0 <= x <= 2^31 - 1
"""
class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        res = 0
        while l <= r:
            m = l + (r - l) //  2
            if m * m > x:
                r = m - 1
            elif m * m < x:
                l = m + 1
                res = m
            else:
                return m
        return res

solution = Solution()
print(solution.mySqrt(4))
print(solution.mySqrt(8))
print(solution.mySqrt(9))
print(solution.mySqrt(13))
