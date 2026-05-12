class Solution:
    def firstMissingPositiveBleh(self, nums: list[int]) -> int:
        hs = set()
        missingNum = float("inf")
        minPositive = float("inf")
        for i in range(len(nums)):
            if nums[i] > 0:
                hs.add(nums[i])
                if nums[i] < minPositive:
                    minPositive = nums[i]

        if minPositive > 1:
            return 1

        for num in hs:
            if (num + 1) not in hs:
                missingNum = num + 1 if num + 1 < missingNum else missingNum
        return int(missingNum)

    def firstMissingPositiveHS(self, nums: list[int]) -> int:
        hs = set()

        for num in nums:
            if num > 0:
                hs.add(num)

        for n in range(1, len(nums) + 2):
            if n not in hs:
                return n
        return -1

    def firstMissingPositive(self, nums: list[int]) -> int:
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0

        for num in nums:
            val = abs(num)
            if 1 <= val <= len(nums):
                if nums[val - 1] > 0:
                    nums[val - 1] *= -1
                elif nums[val - 1] == 0:
                    nums[val - 1] = -1 * (len(nums) + 1)

        for i in range(1, len(nums) + 1):
            if nums[i - 1] >= 0:
                return i

        return len(nums) + 1


solution = Solution()
print(solution.firstMissingPositive([1, 2, 0]))
print(solution.firstMissingPositive([3, 4, -1, 1]))
print(solution.firstMissingPositive([7, 8, 9, 11, 12]))
print(solution.firstMissingPositive([-2, -1, 0]))
print(solution.firstMissingPositive([1, 2, 4]))
print(solution.firstMissingPositive([1, 2, 4, 5, 6, 3, 1]))
