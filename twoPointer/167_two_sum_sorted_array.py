class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        le, ri = 0, len(numbers) - 1
        while le < ri:
            if (numbers[le] + numbers[ri]) == target:
                return [le + 1, ri + 1]
            elif (numbers[le] + numbers[ri]) > target:
                ri -= 1
            else:
                le += 1
        return []


solution = Solution()
print(solution.twoSum([1, 2, 3, 4], 3))
print(solution.twoSum([2, 7, 11, 15], 9))
print(solution.twoSum([2, 3, 4], 6))
print(solution.twoSum([-1, 0], -1))
