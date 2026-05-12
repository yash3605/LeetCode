class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if a > 0:
                break

            if i > 0 and a == nums[i - 1]:
                continue

            le, ri = i + 1, len(nums) - 1
            while le < ri:
                threesum = a + nums[le] + nums[ri]
                if threesum > 0:
                    ri -= 1
                elif threesum < 0:
                    le += 1
                else:
                    res.append([a, nums[le], nums[ri]])
                    le += 1
                    ri -= 1
                    while nums[le] == nums[le - 1] and le < ri:
                        le += 1
        return res


solution = Solution()
print(solution.threeSum([-1, 0, 1, 2, -1, -4]))
print(solution.threeSum([0, 1, 1]))
print(solution.threeSum([0, 0, 0]))
