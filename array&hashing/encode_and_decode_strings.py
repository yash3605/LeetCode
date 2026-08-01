"""
LeetCode #271: Encode and Decode Strings

Design an algorithm to encode a list of strings to a single string. The encoded string is then sent over the network and is decoded back to the original list of strings. Implement the encode and decode methods.

Constraints:
1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of any possible characters out of 256 valid ASCII characters.
"""
class Solution:

    def encode(self, strs: list[str]) -> str:
        resStr = ""
        for str in strs:
            resStr += f"{len(str)}@" + str
        return resStr

    def decode(self, s: str) -> list[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '@':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = length + i
            res.append(s[i:j])
            i = j
        return res


solution = Solution()
input = ["neet","code","love","you"]
encodedString = solution.encode(input)
decodedString = solution.decode(encodedString)

print(encodedString)
print(decodedString)
