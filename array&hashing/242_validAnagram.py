class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mapOfStr = {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            mapOfStr[s[i]] = mapOfStr.get(s[i], 0) + 1
            mapOfStr[t[i]] = mapOfStr.get(t[i], 0) - 1

        return all(value == 0 for value in mapOfStr.values())
