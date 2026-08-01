"""
LeetCode #14: Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings. If there is no common prefix, return an empty string "".

Constraints:
1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
"""
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        longpref = ""
        for i in range(len(strs)):
            prefforeach = ""
            for j in range(len(strs[i])):
                if j >= len(strs[0]) or strs[i][j] != strs[0][j]:
                    break
                prefforeach += strs[i][j]

            if prefforeach < longpref:
                longpref = prefforeach

        return longpref



'''
for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return s[:i]
        return strs[0]
'''
