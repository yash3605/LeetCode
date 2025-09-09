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
