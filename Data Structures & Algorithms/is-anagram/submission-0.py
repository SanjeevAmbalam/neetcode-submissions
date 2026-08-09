from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charS = defaultdict(int) 
        charT = defaultdict(int)
        if len(s) != len(t): return False
        for i in range(len(s)):
            charS[s[i]] += 1
            charT[t[i]] += 1
        return charS == charT
        