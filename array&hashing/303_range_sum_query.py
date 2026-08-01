"""
LeetCode #303: Range Sum Query - Immutable

Design a data structure that handles multiple queries of the following type: Calculate the sum of the elements of nums between indices left and right inclusive where left <= right. Implement the NumArray class: NumArray(int[] nums) initializes the object with the integer array nums. int sumRange(int left, int right) returns the sum of the elements of nums between indices left and right inclusive.

Constraints:
1 <= nums.length <= 10^4
-10^5 <= nums[i] <= 10^5
0 <= left <= right < nums.length
"""
class NumArray:

    def __init__(self, nums: list[int]):
        self.prefixSum = [0] * len(nums)
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            self.prefixSum[i] = sum


    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefixSum[right]
        return self.prefixSum[right] - self.prefixSum[left - 1]


solution = NumArray([-2, 0, 3, -5, 2, -1])
print(solution.sumRange(0, 2))
print(solution.sumRange(2, 5))
print(solution.sumRange(0, 5))
