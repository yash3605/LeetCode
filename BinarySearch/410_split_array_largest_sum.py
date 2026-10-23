class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        def canSplit(largest):
            subArray = 1
            curSum = 0

            for num in nums:
                curSum += num
                if curSum > largest:
                    subArray += 1
                    if subArray > k:
                        return False
                    curSum = num
            return True
        
        l, r  = max(nums), sum(nums)
        res = r
        while l <= r:
            mid = l + (r - l) // 2
            if canSplit(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res
solution = Solution()
print(solution.splitArray([7,2,5,10,8], 2))
print(solution.splitArray([1,2,3,4,5], 2))
print(solution.splitArray([2,4,10,1,5], 2))
print(solution.splitArray([1,0,2,3,5], 4))
