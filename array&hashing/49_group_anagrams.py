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
