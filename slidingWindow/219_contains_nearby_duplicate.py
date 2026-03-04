class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        window = set()
        left = 0

        for right in range(len(nums)):
            if right - left > k :
                window.remove(nums[left])
                left += 1

            if nums[right] in window:
                return True

            window.add(nums[right])
        return False

        

solution = Solution()
print(solution.containsNearbyDuplicate([1,2,3,1], 3))
print(solution.containsNearbyDuplicate([2,1,2], 1))
print(solution.containsNearbyDuplicate([1,0,1,1], 1))
print(solution.containsNearbyDuplicate([1,2,3,1,2,3], 2))
