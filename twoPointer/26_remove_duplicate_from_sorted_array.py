class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        curr = 0
        for j in range(1, len(nums)):
            if nums[curr] != nums[j]:
                curr += 1
                nums[curr] = nums[j]
        return curr + 1


solution = Solution()
print(solution.removeDuplicates([1, 1, 2]))
print(solution.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
print(solution.removeDuplicates([1, 1, 2, 3, 4]))
print(solution.removeDuplicates([2, 10, 10, 30, 30, 30]))
