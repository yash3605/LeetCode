"""
LeetCode #1768: Merge Strings Alternately

You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string. Return the merged string.

Constraints:
1 <= word1.length, word2.length <= 100, word1 and word2 consist of lowercase English letters.
"""
class Solution:
    def mergeAlternatelyRAW(self, word1: str, word2: str) -> str:
        res = ""
        word1_ptr = 0
        word2_ptr = 0
        while word1_ptr < len(word1) and word2_ptr < len(word2):
            res += word1[word1_ptr]
            res += word2[word2_ptr]
            word1_ptr += 1
            word2_ptr += 1
        while word1_ptr < len(word1):
            res += word1[word1_ptr]
            word1_ptr += 1
        while word2_ptr < len(word2):
            res += word2[word2_ptr]
            word2_ptr += 1

        return res

    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        i = j = 0
        while i < len(word1) and j < len(word2):
            res.append(word1[i])
            res.append(word2[j])
            i += 1
            j += 1
        res.append(word1[i:])
        res.append(word2[j:])

        return "".join(res)


solution = Solution()
print(solution.mergeAlternately("abc", "pqr"))
print(solution.mergeAlternately("ab", "pqrs"))
print(solution.mergeAlternately("abcd", "pq"))
print(solution.mergeAlternately("abc", "xyz"))
print(solution.mergeAlternately("ab", "abbxxc"))
