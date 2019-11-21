class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        obj = {}
        for i in range(len(s)):
            if s[i] not in obj:
                obj[s[i]] = t[i]
            elif obj[s[i]] != t[i]:
                return False
        obj = {}
        for i in range(len(s)):
            if t[i] not in obj:
                obj[t[i]] = s[i]
            elif obj[t[i]] != s[i]:
                return False
        
        return True