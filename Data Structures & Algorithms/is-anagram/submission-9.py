class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s1 = {}
        t1 = {}
        for i in range(len(s)):
            s1[s[i]] = 1 + s1.get(s[i], 0)
        for j in range(len(t)):
            t1[t[j]] = 1 + t1.get(t[j], 0)
        return (s1 == t1)