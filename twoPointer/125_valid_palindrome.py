class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = "".join(filter(str.isalnum, s)).lower()
        i, j = 0, len(new_str) - 1
        while i <= j:
            if new_str[i] != new_str[j]:
                return False
            i += 1
            j -= 1
        return True


solution = Solution()
print(solution.isPalindrome("race a car"))
print(solution.isPalindrome("a man, a plan, a canal: panama"))
print(solution.isPalindrome(" "))
print(solution.isPalindrome("Was it a car or a cat I saw?"))
print(solution.isPalindrome("tab a cat"))
