class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m

        pivot = l

        def binary_search(left: int, right: int) -> int:
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1

        result = binary_search(0, pivot - 1)
        if result != -1:
            return result

        return binary_search(pivot, len(nums) - 1)


solution = Solution()
print(solution.search([3,4,5,6,1,2], 1))
print(solution.search([3,5,6,0,1,2], 4))
print(solution.search([4,5,6,7,0,1,2], 0))
print(solution.search([4,5,6,7,0,1,2], 3))
print(solution.search([1], 0))

'''

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        L, R = 0, len(nums) - 1
        while L <= R:
            M = (L + R) // 2
            if nums[M] > nums[R]:
                L = M + 1
            else:
                R = M

        pivot = L

        def binary_search(left: int, right: int) -> int:
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1
            
        result = binary_search(0, pivot - 1)
        if result != -1:
            return result

        return binary_search(pivot, len(nums) - 1)
'''
