"""
LeetCode #49: Group Anagrams

Given an array of strings strs, group the anagrams together. You can return the answer in any order. An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Constraints:
1 <= strs.length <= 10^4
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        hs = defaultdict(list)
        for s in strs:
            key_arr = [0] * 26
            for i in range(len(s)):
                key_arr[ord(s[i]) - ord("a")] += 1
            hs[f"{key_arr}"].append(s)

        return list(hs.values())
obj1 = Solution()
print(obj1.groupAnagrams(["act","pots","tops","cat","stop","hat"]))
print(obj1.groupAnagrams(["x"]))
print(obj1.groupAnagrams([""]))
