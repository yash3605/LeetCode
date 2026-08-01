"""
LeetCode #374: Guess Number Higher or Lower

We are playing the Guess Game. The game is as follows: I pick a number from 1 to n. You guess a number. If you guess the right number, you win. If you guess the wrong number, I will tell you whether the number I picked is higher or lower. You are given a pre-defined API int guess(int num), which returns 3 possible results: -1 (the number is higher), 1 (the number is lower), 0 (the number is the guess). Return the number that I picked.

Constraints:
1 <= n <= 2^31 - 1
1 <= pick <= n
"""
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 1, n
        while l <= r:
            m = (l + r) // 2
            res = guess(m)

            if res < 0:
                r = m - 1
            elif res > 0:
                l = m + 1
            else:
                return m

solution = Solution()
print(solution.guessNumber(5))
print(solution.guessNumber(15))
print(solution.guessNumber(1))
print(solution.guessNumber(10))
print(solution.guessNumber(1))
print(solution.guessNumber(2))
