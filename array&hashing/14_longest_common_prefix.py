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
