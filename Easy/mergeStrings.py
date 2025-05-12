class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""

        pointer_one = 0
        pointer_two = 0

        while pointer_one < len(word1) and pointer_two < len(word2):
            res += word1[pointer_one]
            res += word2[pointer_two]

            pointer_one += 1
            pointer_two += 1
        res += word1[pointer_one:]
        res += word2[pointer_two:]
        return res

