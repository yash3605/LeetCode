"""
LeetCode #18: 4Sum

Given an array nums of n integers and an integer target, return all unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that: 0 <= a, b, c, d < n, a, b, c, and d are distinct, and nums[a] + nums[b] + nums[c] + nums[d] == target. You may return the answer in any order.

Constraints:
1 <= nums.length <= 200, -10^9 <= nums[i] <= 10^9, -10^9 <= target <= 10^9
"""
class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        res = []
        nums.sort()

        for a in range(len(nums)):
            if a > 0 and nums[a] == nums[a - 1]:
                continue

            for b in range(a + 1, len(nums)):
                if b > a + 1 and nums[b] == nums[b - 1]:
                    continue

                c, d = b + 1, len(nums) - 1
                while c < d:
                    foursum = nums[a] + nums[b] + nums[c] + nums[d]
                    if foursum == target:
                        res.append([nums[a], nums[b], nums[c], nums[d]])
                        c += 1
                        d -= 1

                        while nums[c] == nums[c - 1] and c < d:
                            c += 1

                        while nums[d] == nums[d + 1] and c < d:
                            d -= 1
                    elif foursum < target:
                        c += 1
                    else:
                        d -= 1

        return res


solution = Solution()
print(solution.fourSum([1, 0, -1, 0, -2, 2], 0))
print(solution.fourSum([2, 2, 2, 2, 2], 8))
print(solution.fourSum([3, 2, 3, -3, 1, 0], 3))
print(solution.fourSum([1, -1, 1, -1, 1, -1], 2))
