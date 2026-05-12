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
