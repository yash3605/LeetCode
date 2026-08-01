"""
LeetCode #242: Valid Anagram

Given two strings s and t, return true if t is an anagram of s, and false otherwise. An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase.

Constraints:
1 <= s.length, t.length <= 5 * 10^4
s and t consist of lowercase English letters.
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mapOfStr = {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            mapOfStr[s[i]] = mapOfStr.get(s[i], 0) + 1
            mapOfStr[t[i]] = mapOfStr.get(t[i], 0) - 1

        return all(v == 0 for v in mapOfStr.values())
